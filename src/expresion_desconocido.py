from telegram import Update
from telegram.ext import ContextTypes
from .expresion import Expresion


class ExpresionDesconocido(Expresion):
    """
    Expresión que responde a un comando desconocido.
    """

    async def interpretar(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        respuesta = "No entiendo el comando que has proporcionado.\n" + \
                    "Utiliza /ayuda para ver los comandos disponibles."
        await self._enviar_mensaje(update, respuesta)

    def descripcion(self) -> str:
        return "/comando - Responde a un comando desconocido."
