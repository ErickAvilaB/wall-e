from abc import ABC, abstractmethod
from telegram import Update
from telegram.ext import ContextTypes


class ExpresionAbstracta(ABC):

    @abstractmethod
    async def interpretar(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        pass

    @abstractmethod
    def descripcion(self) -> str:
        pass

    async def _enviar_mensaje(self, update: Update, mensaje: str) -> None:
        await update.message.reply_text(mensaje)
