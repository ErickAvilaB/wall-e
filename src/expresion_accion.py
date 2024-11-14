from .expresion import Expresion
from .cliente_yfinance import ClienteYFinance


class ExpresionAccion(Expresion):
    def evaluar(self, contexto: dict):
        ticker: str = contexto['ticker']
        periodo: str = contexto['periodo']
        accion = ClienteYFinance.get_accion(ticker, periodo)
        return accion
