from abc import ABC, abstractmethod
from telegram import Update
from telegram.ext import ContextTypes


class Expresion(ABC):
    """
    Clase abstracta que define el comportamiento de una expresión.
    """

    @abstractmethod
    async def interpretar(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """
        Interpreta el mensaje del usuario y responde según la expresión.
        Args:
            update (telegram.Update): Actualización del mensaje.
            context (telegram.ext.Context): Contexto de la conversación.
        """
        pass

    @abstractmethod
    def descripcion(self) -> str:
        """
        Retorna la descripción de la expresión.
        Returns:
            str: Descripción de la expresión.
        """
        pass

    async def _enviar_mensaje(self, update: Update, mensaje: str) -> None:
        """
        Envía un mensaje al usuario.
        Args:
            update (telegram.Update): Actualización del mensaje.
            mensaje (str): Mensaje a enviar.
        """
        await update.message.reply_text(mensaje)
