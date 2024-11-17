from telegram import Update
from telegram.ext import ContextTypes
from .comando import Comando


class ComandoDesconocido(Comando):
    async def responder(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await self._enviar_mensaje(update, "Comando desconocido. Usa /ayuda para ver la lista de comandos disponibles.")
