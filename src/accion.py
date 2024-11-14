import matplotlib.pyplot as plt


class Accion:
    def __init__(self, data: dict, valor_historico) -> None:
        self.__data: dict = data
        self.__historico = valor_historico

    @property
    def nombre_empresa(self) -> str:
        return self.__data['longName']

    @property
    def ticker(self) -> str:
        return self.__data['symbol']

    @property
    def sector(self) -> str:
        return self.__data['sector']

    @property
    def pais(self) -> str:
        return self.__data['country']

    @property
    def divisa(self) -> str:
        return self.__data['currency']

    @property
    def precio_actual(self) -> float:
        return self.__data['currentPrice']

    def generar_grafico(self, carpeta: str = ".") -> str:
        self.__historico.reset_index(inplace=True)
        plt.figure(figsize=(10, 5))
        plt.plot(self.__historico['Date'], self.__historico['Close'],
                 label=f"Evolución", color='darkgreen', linewidth=3)
        ultimo_precio: float = self.__historico['Close'].iloc[-1]
        ultima_fecha: str = self.__historico['Date'].iloc[-1]
        plt.axhline(y=ultimo_precio, color='red', linestyle='--',
                    label=f"Precio actual: {self.divisa} {ultimo_precio:.2f}")
        plt.text(ultima_fecha, ultimo_precio,
                 f"{self.divisa} {ultimo_precio:.2f}", fontsize=12,
                 verticalalignment='bottom', horizontalalignment='right')
        plt.title(f"{self.ticker} - {self.nombre_empresa}")
        plt.xlabel("Fecha")
        plt.ylabel("Precio de cierre")
        plt.grid()
        plt.legend()
        ruta_archivo: str = f"{carpeta}/{self.ticker}.png"
        plt.savefig(ruta_archivo)
        plt.close()
        return ruta_archivo

    def __str__(self) -> str:
        return f"{self.ticker} - {self.nombre_empresa}\n" \
               f"Sector: {self.sector}\n" \
               f"País: {self.pais}\n" \
               f"Precio actual: {self.divisa} {self.precio_actual:.2f}"
