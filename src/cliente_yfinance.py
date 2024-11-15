from yfinance import Ticker
from .accion import Accion


class ClienteYFinance:
    @staticmethod
    def get_accion(ticker: str, periodo_historico: str = "3mo") -> Accion:
        """
        Obtiene la información de una acción con base a su ticker
        - Parámetros:
            - ticker (str): Ticker de la acción
            - periodo_historico (str): Periodo histórico de la acción
        - Retorna:
            - Accion: Objeto Accion con la información de la acción
        """
        accion: Ticker = Ticker(ticker)
        try:
            datos_historicos = accion.history(
                period=periodo_historico, interval="1d")
            info: dict = accion.info
            return Accion(info, datos_historicos)
        except Exception as e:
            raise Exception(f"Error al obtener la acción {ticker}: {e}")
