"""
Punto de entrada del bot.

Este archivo solo conecta las piezas: registra los comandos y decide,
para un mensaje de texto libre, en qué orden probar las distintas
respuestas (menú, cálculo de precio, saludo, respuesta por defecto).

Para agregar una nueva respuesta a mensajes libres, crea una función
handler nueva en la carpeta handlers/ y agrégala al flujo de
unknown_message() más abajo.
"""

import logging

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import TOKEN
from handlers.start import start_command
from handlers.productos import productos_command
from handlers.servicios import servicios_command
from handlers.greetings import handle_greeting
from handlers.pricing import maybe_answer_pricing

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def unknown_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Se ejecuta para cualquier mensaje de texto que NO sea un comando
    (/productos, /servicios, etc). Prueba, en orden, distintas formas
    de responder.
    """
    text = (update.message.text or "").strip().lower()

    # 1. Botones del menú principal (mandan texto plano, no comandos)
    if text in ("📦 productos", "productos"):
        await productos_command(update, context)
        return
    if text in ("🔧 servicios", "servicios"):
        await servicios_command(update, context)
        return

    # 2. ¿Pregunta por precio/instalación? Ej: "cuanto cuesta instalar x"
    if await maybe_answer_pricing(update, context):
        return

    # 3. ¿Es un saludo?
    if await handle_greeting(update, context):
        return

    # 4. Respuesta por defecto si no entendimos nada
    await update.message.reply_text(
        "No estoy seguro de haber entendido 🤔\n"
        "Prueba con /productos, /servicios, o pregúntame algo como:\n"
        "\"¿Cuánto cuesta la instalación de [producto]?\""
    )


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("productos", productos_command))
    app.add_handler(CommandHandler("servicios", servicios_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_message))

    logger.info("Bot iniciado correctamente. Presiona Ctrl+C para detenerlo.")
    app.run_polling()


if __name__ == "__main__":
    main()
