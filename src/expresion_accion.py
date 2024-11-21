from os import remove
from telegram import Update
from telegram.ext import ContextTypes
from .expresion import Expresion
from .cliente_yfinance import ClienteYfinance
from .accion_graficable import AccionGraficable


class ExpresionAccion(Expresion):
    """
    Responde al comando /accion con información y un gráfico opcional de la acción.
    """

    async def interpretar(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.args:
            await self._enviar_mensaje(update, "Debes proporcionar el ticker de la acción.")
            return

        # Extraer y validar argumentos
        ticker, periodo, incluir_grafico = self.__procesar_argumentos(
            context.args)

        # Obtener y enviar información de la acción
        try:
            await self.__procesar_accion(update, ticker, periodo, incluir_grafico)
        except Exception as e:
            await self._enviar_mensaje(update, str(e))

    PERIODOS_VALIDOS = ["1d", "5d", "1mo", "3mo", "6mo",
                        "1y", "2y", "5y", "10y", "ytd", "max"]

    def __procesar_argumentos(self, args: list) -> tuple:
        """
        Procesa los argumentos ingresados por el usuario.
        Returns:
            tuple: ticker, periodo, incluir_grafico
        """
        ticker: str = args[0]
        incluir_grafico: bool = "-g" in args
        periodo: str = next(
            (i for i in args[1:] if i in self.PERIODOS_VALIDOS), "3mo")
        return ticker, periodo, incluir_grafico

    async def __procesar_accion(self, update: Update, ticker: str, periodo: str, incluir_grafico: bool) -> None:
        info_accion = ClienteYfinance.get_info(ticker)
        mensaje = str(info_accion)
        await self._enviar_mensaje(update, mensaje)

        # Si se solicitó, generar y enviar gráfico
        if incluir_grafico:
            valor_historico = ClienteYfinance.get_valor_historico(
                ticker, periodo)
            accion_graficable = AccionGraficable(
                info_accion.info, valor_historico)
            ruta_grafico = accion_graficable.generar_grafico()

            try:
                with open(ruta_grafico, 'rb') as archivo:
                    await update.message.reply_photo(photo=archivo)
            finally:
                remove(ruta_grafico)

    def descripcion(self) -> str:
        return (
            "/accion <ticker> [periodo] [-g] - Obtiene información de una acción.\n"
            "  - Ticker: AAPL, AMZN, GOOGL, TSLA, MSFT...\n"
            "  - Periodo: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max\n"
            "  - -g: Incluye un gráfico de la acción."
        )
