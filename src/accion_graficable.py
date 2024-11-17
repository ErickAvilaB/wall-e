import pandas as pd
import matplotlib.pyplot as plt
from .accion import Accion


class AccionGraficable(Accion):
    """
    Clase que extiende la funcionalidad de la clase Accion para incluir gráficos del precio histórico.
    """

    def __init__(self, info: dict, valor_historico: pd.DataFrame) -> None:
        """
        Inicializa una instancia de AccionGraficable.
        Args:
            info (dict): Diccionario con la información de la acción.
            valor_historico (pd.DataFrame): DataFrame con los datos históricos de la acción.
        """
        super().__init__(info)
        self.__valor_historico = valor_historico

    def generar_grafico(self, carpeta: str = ".") -> str:
        """
        Genera un gráfico de la evolución del precio de cierre de la acción y lo guarda como imagen.
        Args:
            carpeta (str): Carpeta donde se guardará el archivo (por defecto, la carpeta actual).
        Returns:
            str: Ruta del archivo de imagen generado.
        """
        # Validar que el DataFrame no esté vacío
        if self.__valor_historico.empty:
            raise ValueError("El DataFrame de valor histórico está vacío.")

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
        """
        Traza la evolución del precio de cierre en el gráfico.
        Args:
            ax (matplotlib.axes.Axes): Eje del gráfico.
        """
        ax.plot(
            self.__valor_historico['Date'],
            self.__valor_historico['Close'],
            label="Evolución",
            color='darkgreen',
            linewidth=3
        )

    def _anotar_precio_actual(self, ax) -> None:
        """
        Añade una línea y una etiqueta indicando el precio actual en el gráfico.
        Args:
            ax (matplotlib.axes.Axes): Eje del gráfico.
        """
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
