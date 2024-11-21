import pandas as pd
import matplotlib.pyplot as plt
from .accion import Accion


class AccionGraficable(Accion):

    def __init__(self, info: dict, valor_historico: pd.DataFrame) -> None:
        super().__init__(info)
        self.__valor_historico = valor_historico

    def generar_grafico(self, carpeta: str = ".") -> str:
        # Resetear el índice para que 'Date' sea una columna
        self.__valor_historico.reset_index(inplace=True)

        # Crear el gráfico
        fig, ax = plt.subplots(figsize=(10, 5))
        self._trazar_evolucion(ax)
        self._anotar_precio_actual(ax)

        # Configurar título y etiquetas del gráfico
        ax.set_title(f"{self.ticker} - {self.nombre_empresa}")
        ax.set_xlabel("Fecha")
        ax.set_ylabel("Precio de cierre")
        ax.grid(visible=True)
        ax.legend()

        # Guardar el gráfico como archivo PNG
        ruta_archivo = f"{carpeta}/{self.ticker}.png"
        plt.savefig(ruta_archivo)
        plt.close(fig)  # Cerrar la figura para liberar memoria

        return ruta_archivo

    def _trazar_evolucion(self, ax) -> None:
        ax.plot(
            self.__valor_historico['Date'],
            self.__valor_historico['Close'],
            label="Evolución",
            color='darkgreen',
            linewidth=3
        )

    def _anotar_precio_actual(self, ax) -> None:
        # Obtener el último precio y la última fecha
        ultimo_precio = self.__valor_historico['Close'].iloc[-1]
        ultima_fecha = self.__valor_historico['Date'].iloc[-1]

        # Dibujar una línea horizontal indicando el precio actual
        ax.axhline(
            y=ultimo_precio,
            color='red',
            linestyle='--',
            label=f"Precio actual: {self.divisa} {ultimo_precio:.2f}"
        )

        # Añadir una etiqueta con el precio actual
        ax.text(
            x=ultima_fecha,
            y=ultimo_precio,
            s=f"{self.divisa} {ultimo_precio:.2f}",
            fontsize=12,
            verticalalignment='bottom',
            horizontalalignment='right'
        )
