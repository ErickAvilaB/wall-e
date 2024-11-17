from telegram import Update
from telegram.ext import ContextTypes
from .comando import Comando


class ComandoEcho(Comando):
    async def responder(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await self._enviar_mensaje(update, update.message.text)

    def descripcion(self, mensaje: str = "") -> str:
        return "Repite el mensaje proporcionado."
