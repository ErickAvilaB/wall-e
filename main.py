import logging
from os import getenv
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from src import ComandoEcho, ComandoDesconocido, ComandoAyuda, ComandoAccion


def main() -> None:
    load_dotenv()

    api_token: str = getenv('API_TOKEN')

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    application = ApplicationBuilder().token(api_token).build()

    comando_echo: ComandoEcho = ComandoEcho()

    ayuda_handler = CommandHandler('ayuda', ComandoAyuda().responder)
    start_handler = CommandHandler('start', ComandoAyuda().responder)
    accion_handler = CommandHandler('accion', ComandoAccion().responder)
    echo_handler = MessageHandler(filters.TEXT & (
        ~filters.COMMAND), comando_echo.responder)
    unknown_handler = MessageHandler(
        filters.COMMAND, ComandoDesconocido().responder)

    application.add_handler(ayuda_handler)
    application.add_handler(start_handler)
    application.add_handler(accion_handler)
    application.add_handler(echo_handler)
    application.add_handler(unknown_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
