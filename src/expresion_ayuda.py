from .expresion import Expresion


class ExpresionAyuda(Expresion):
    def evaluar(self, contexto: dict) -> str:
        mensaje: str = "Soy un bot que te permite obtener información de acciones de la bolsa de valores.\n" \
            "\n" \
            "Los comandos disponibles son:\n" \
            "\n" \
            "/accion <ticker> [periodo] [-ng] - Obtiene información de una acción.\n" \
            "  - Ticker: AAPL, AMZN, GOOGL, TSLA, MSFT...\n" \
            "  - Periodo: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max\n" \
            "  - -ng: No incluir gráfico"
        return mensaje
