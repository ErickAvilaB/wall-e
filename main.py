import logging
from os import getenv
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from src.cliente_yfinance import ClienteYFinance

load_dotenv()

api_token: str = getenv('API_TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def accion(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(context.args) == 0:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Debes ingresar el ticker de la acción")
        return
    try:
        ticker = context.args[0]
        accion = ClienteYFinance.get_accion(ticker, "1y")
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"{accion.ticker} - {accion.nombre_empresa}\n"
                 f"Sector: {accion.sector}\n"
                 f"País: {accion.pais}\n"
                 f"Precio actual: {accion.divisa} {accion.precio_actual}\n"
        )
    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Error al obtener la acción {ticker}")


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


def main() -> None:
    application = ApplicationBuilder().token(api_token).build()

    start_handler = CommandHandler('start', start)
    accion_handler = CommandHandler('accion', accion)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    application.add_handler(start_handler)
    application.add_handler(accion_handler)
    application.add_handler(unknown_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
