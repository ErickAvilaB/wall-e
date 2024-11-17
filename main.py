import logging
from os import getenv
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from src import ExpresionEcho, ExpresionDesconocido, ExpresionAyuda, ExpresionAccion


def configurar_logging() -> None:
    """
    Imprime los mensajes de log en la consola. En formato: [fecha] - [nombre] - [nivel] - [mensaje]
    """
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )


def crea_bot(api_token: str) -> ApplicationBuilder:
    """
    Crea un bot de Telegram con el token proporcionado.
    Args:
        api_token (str): Token de la API de Telegram.
    Returns:
        ApplicationBuilder: Bot de Telegram.
    """
    return ApplicationBuilder().token(api_token).build()


def crea_manejador() -> list:
    """
    Analiza los comandos proporcionados por el usuario.
    Returns:
        list: Lista de manejadores de comandos.
    """
    ayuda_handler = CommandHandler('ayuda', ExpresionAyuda().interpretar)
    start_handler = CommandHandler('start', ExpresionAyuda().interpretar)
    accion_handler = CommandHandler('accion', ExpresionAccion().interpretar)
    echo_handler = MessageHandler(filters.TEXT & (
        ~filters.COMMAND), ExpresionEcho().interpretar)
    unknown_handler = MessageHandler(
        filters.COMMAND, ExpresionDesconocido().interpretar)

    return [ayuda_handler, start_handler, accion_handler, echo_handler, unknown_handler]


def main() -> None:
    """
    Define el punto de entrada de la aplicación.
    """
    configurar_logging()

    load_dotenv()

    api_token: str = getenv('API_TOKEN')

    application = crea_bot(api_token)

    for handler in crea_manejador():
        application.add_handler(handler)

    application.run_polling()


if __name__ == '__main__':
    main()
