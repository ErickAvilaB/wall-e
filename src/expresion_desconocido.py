from telegram import Update
from telegram.ext import ContextTypes
from .expresion_abstracta import ExpresionAbstracta


class ExpresionDesconocido(ExpresionAbstracta):
    """
    Expresión que responde a un comando desconocido.
    """

    async def interpretar(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        respuesta = "No entiendo el comando que has proporcionado." + \
                    "Utiliza /ayuda para ver los comandos disponibles."
        await self._enviar_mensaje(update, respuesta)

    def descripcion(self) -> str:
        return "[comando invalido] - Responde a un comando desconocido."
