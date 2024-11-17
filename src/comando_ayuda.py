from telegram import Update
from telegram.ext import ContextTypes
from .comando import Comando


class ComandoAyuda(Comando):
    async def responder(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        mensaje: str = "Soy un bot que te permite obtener información de acciones de la bolsa de valores.\n\n" \
            "Los comandos disponibles son:\n\n" \
            "/accion <ticker> [periodo] [-ng] - Obtiene información de una acción.\n" \
            "  - Ticker: AAPL, AMZN, GOOGL, TSLA, MSFT...\n" \
            "  - Periodo: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max\n" \
            "  - -ng: No incluir gráfico"
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=mensaje
        )
