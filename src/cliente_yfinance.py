from yfinance import Ticker
from .accion import Accion


class ClienteYfinance:
    """
    Cliente para interactuar con la API de yfinance y obtener datos de acciones.
    """

    @staticmethod
    def get_info(ticker: str) -> Accion:
        ClienteYfinance._validar_ticker(ticker)
        accion: Ticker = Ticker(ticker)
        info: dict = {}
        try:
            info = accion.info
        except Exception as e:
            raise ValueError(
                f"Ocurrió un error al obtener la información de la acción {ticker}: {e}")
        if not info.get("longName"):
            raise ValueError(
                f"No se encontró información para la acción {ticker}")
        return Accion(info)

    @staticmethod
    def get_valor_historico(ticker: str, periodo: str = "3mo"):
        """
        Obtiene el valor histórico de una acción.
        Args:
            ticker (str): Símbolo de la acción.
            periodo (str): Periodo histórico (por defecto, "3mo"). 
                Valores válidos: "1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", 
                "5y", "10y", "ytd", "max".
        Returns:
            pd.DataFrame: DataFrame con los datos históricos de la acción.
        Raises:
            ValueError: Si no se pueden obtener los datos históricos.
        """
        ClienteYfinance._validar_ticker(ticker)
        ClienteYfinance._validar_periodo(periodo)
        accion: Ticker = Ticker(ticker)
        datos_historicos = None
        try:
            datos_historicos = accion.history(period=periodo, interval="1d")
        except Exception as e:
            raise ValueError(
                f"Ocurrió un error al obtener los datos históricos de la acción {ticker}: {e}")
        if datos_historicos.empty or datos_historicos is None:
            raise ValueError(
                f"No se encontraron datos históricos para la acción {ticker}")

    def _validar_ticker(ticker: str) -> bool:
        if not ticker.isalpha() or len(ticker) > 5:
            raise ValueError(
                "El ticker debe ser una cadena alfabética de máximo 5 caracteres.")

    def _validar_periodo(periodo: str) -> bool:
        periodos: list = ["1d", "5d", "1mo", "3mo",
                          "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
        if periodo not in periodos:
            raise ValueError(
                f"El periodo '{periodo}' no es válido. Valores válidos: {', '.join(periodos)}")
