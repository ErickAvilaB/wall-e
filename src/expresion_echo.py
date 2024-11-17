from telegram import Update
from telegram.ext import ContextTypes
from .expresion import Expresion


class ExpresionEcho(Expresion):
    """
    Expresión que repite el mensaje proporcionado.
    """

    async def interpretar(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await self._enviar_mensaje(update, update.message.text)

    def descripcion(self, mensaje: str = "") -> str:
        return "[mensaje] - Repite el mensaje proporcionado."
