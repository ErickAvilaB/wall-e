from yfinance import Ticker
from .accion import Accion


class ClienteYFinance:
    @staticmethod
    def get_accion(ticker: str, periodo_historico: str = "max") -> Accion:
        """
        Obtiene la información de una acción en base a su ticker
        - Parámetros:
            - ticker (str): Ticker de la acción
            - periodo_historico (str): Periodo histórico de la acción
        - Retorna:
            - Accion: Objeto Accion con la información de la acción
        """
        try:
            accion: Ticker = Ticker(ticker)
            info: dict = accion.info
            datos_historicos = accion.history(period=periodo_historico)
            return Accion(
                nombre_empresa=info['longName'],
                ticker=info['symbol'],
                sector=info['sector'],
                pais=info['country'],
                divisa=info['currency'],
                precio_actual=info['currentPrice'],
                historico=datos_historicos
            )
        except Exception as e:
            raise Exception(f"Error al obtener la acción {ticker}: {e}")
