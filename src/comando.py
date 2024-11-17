from abc import ABC, abstractmethod
from telegram import Update
from telegram.ext import ContextTypes


class Comando(ABC):
    @abstractmethod
    async def responder(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        pass

    async def _enviar_mensaje(self, update: Update, mensaje: str) -> None:
        """
        Envía un mensaje al chat del usuario.
        """
        await update.message.reply_text(mensaje)
