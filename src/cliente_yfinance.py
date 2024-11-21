from yfinance import Ticker
from .accion import Accion


class ClienteYFinance:
    """
    Cliente para interactuar con la API de yfinance y obtener datos de acciones.
    """

    @staticmethod
    def get_info(ticker: str) -> Accion:
        accion: Ticker = Ticker(ticker)
        try:
            info: dict = accion.info
            if not info:
                raise ValueError(
                    f"No se encontró información para el ticker {ticker}.")
            return Accion(info)
        except Exception as e:
            raise ValueError(
                f"Error al obtener la información de la acción {ticker}: {e}")

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
        accion: Ticker = Ticker(ticker)
        try:
            # Obtener datos históricos con el período y el intervalo especificado
            datos_historicos = accion.history(period=periodo, interval="1d")
            # Validar si se obtuvieron datos
            if datos_historicos.empty:
                raise ValueError(
                    f"No se encontraron datos históricos para {ticker} en el periodo {periodo}.")
            return datos_historicos
        except Exception as e:
            raise ValueError(
                f"Error al obtener el valor histórico de la acción {ticker}: {e}")
