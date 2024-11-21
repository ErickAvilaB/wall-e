from telegram import Update
from telegram.ext import ContextTypes
from .expresion import Expresion
from .expresion_accion import ExpresionAccion


class ExpresionAyuda(Expresion):
    """
    Expresión que responde al comando /ayuda.
    """

    async def interpretar(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        descripcion_ayuda: str = self.descripcion()
        descripcion_accion: str = ExpresionAccion().descripcion()

        respuesta = (
            "Comandos disponibles:\n\n"
            f"{descripcion_accion}\n\n"
            f"{descripcion_ayuda}"
        )
        await self._enviar_mensaje(update, respuesta)

    def descripcion(self) -> str:
        return "/ayuda - Muestra los comandos disponibles."
