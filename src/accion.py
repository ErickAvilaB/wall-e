class Accion:
    """
    Clase que representa la información de una acción utilizando datos obtenidos de yfinance.
    """

    def __init__(self, info: dict) -> None:
        """
        Inicializa una instancia de la clase Accion.
        Args:
            info (dict): Diccionario con la información de la acción.
        """
        self.__info: dict = info

    def __obtener_info(self, clave: str, valor_por_defecto=None):
        """Método auxiliar para obtener información del diccionario."""
        return self.__info.get(clave, valor_por_defecto)

    @property
    def nombre_empresa(self) -> str:
        """Nombre completo de la empresa."""
        return self.__obtener_info('longName', "N/A")

    @property
    def ticker(self) -> str:
        """Símbolo (ticker) de la acción."""
        return self.__obtener_info('symbol', "N/A")

    @property
    def sector(self) -> str:
        """Sector al que pertenece la empresa."""
        return self.__obtener_info('sector', "N/A")

    @property
    def industria(self) -> str:
        """Industria de la empresa."""
        return self.__obtener_info('industry', "N/A")

    @property
    def precio_actual(self) -> float:
        """Precio actual de la acción."""
        return self.__obtener_info('regularMarketPrice', 0.0)

    @property
    def precio_maximo(self) -> float:
        """Precio máximo en las últimas 52 semanas."""
        return self.__obtener_info('fiftyTwoWeekHigh', 0.0)

    @property
    def precio_minimo(self) -> float:
        """Precio mínimo en las últimas 52 semanas."""
        return self.__obtener_info('fiftyTwoWeekLow', 0.0)

    @property
    def capitalizacion(self) -> float:
        """Capitalización de mercado de la empresa."""
        return self.__obtener_info('marketCap', 0.0)

    @property
    def pais(self) -> str:
        """País de origen de la empresa."""
        return self.__obtener_info('country', "N/A")

    @property
    def divisa(self) -> str:
        """Divisa en la que cotiza la acción."""
        return self.__obtener_info('currency', "N/A")

    @property
    def info(self) -> dict:
        """Diccionario completo con toda la información de la acción."""
        return self.__info

    def __str__(self) -> str:
        """Representación en cadena del objeto Accion."""
        return (
            f"{self.ticker} - {self.nombre_empresa}\n"
            f"  - País: {self.pais}\n"
            f"  - Sector: {self.sector}\n"
            f"  - Industria: {self.industria}\n"
            f"  - Divisa: {self.divisa}\n"
            f"  - Precio actual: {self.divisa} {self.precio_actual:.2f}\n"
            f"  - Precio máximo (52 semanas): {self.divisa} {self.precio_maximo:.2f}\n"
            f"  - Precio mínimo (52 semanas): {self.divisa} {self.precio_minimo:.2f}\n"
            f"  - Capitalización: {self.divisa} {self.capitalizacion:,.2f}"
        )
