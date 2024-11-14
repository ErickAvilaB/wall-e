import logging
from os import getenv, remove
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from src import ExpresionAyuda, ExpresionAccion


def crear_carpeta_graficos() -> str:
    import os
    if not os.path.exists("graficos"):
        os.makedirs("graficos")
    return "graficos"


CARPETA_GRAFICOS: str = crear_carpeta_graficos()


def periodos_validos(periodo: str) -> bool:
    return periodo in ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max", "-ng"]


def uso_comando_accion() -> str:
    return "Uso\n" \
        "/accion <ticker> [periodo] [-ng] - Obtiene información de una acción.\n" \
        "  - Ticker: AAPL, AMZN, GOOGL, TSLA, MSFT...\n" \
        "  - Periodo: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max\n" \
        "  - -ng: No incluir gráfico"


async def accion(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=uso_comando_accion()
        )
        return

    ticker: str = context.args[0]
    periodo: str = "3mo" if len(context.args) == 1 else context.args[1]
    incluir_grafico: bool = "-ng" not in context.args
    contexto: dict = {
        'ticker': ticker,
        'periodo': periodo
    }

    if not periodos_validos(periodo):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=uso_comando_accion()
        )
        return

    try:
        expresion_accion = ExpresionAccion()
        accion = expresion_accion.evaluar(contexto)
        mensaje_accion: str = str(accion)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=mensaje_accion
        )
        if incluir_grafico:
            grafico: str = accion.generar_grafico(CARPETA_GRAFICOS)
            await context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=open(grafico, 'rb')
            )
            remove(grafico)
    except Exception as e:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Se presentó un error al obtener la acción {ticker}: {e}"
        )


async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    expresion_ayuda = ExpresionAyuda()
    mensaje_ayuda: str = expresion_ayuda.evaluar(None)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=mensaje_ayuda
    )


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Comando inválido."
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Echo: {update.message.text}"
    )


def main() -> None:
    load_dotenv()

    api_token: str = getenv('API_TOKEN')

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    application = ApplicationBuilder().token(api_token).build()

    ayuda_handler = CommandHandler('ayuda', ayuda)
    start_handler = CommandHandler('start', ayuda)
    accion_handler = CommandHandler('accion', accion)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    application.add_handler(ayuda_handler)
    application.add_handler(start_handler)
    application.add_handler(accion_handler)
    application.add_handler(echo_handler)
    application.add_handler(unknown_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
