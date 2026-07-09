from telegram import Update
from telegram.ext import ContextTypes

from utils.keyboards import MAIN_MENU


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Hola! 👋 Soy el bot de *Tu Negocio*.\n\n"
        "Puedo ayudarte a:\n"
        "📦 Ver productos → /productos\n"
        "🔧 Ver servicios → /servicios\n\n"
        "También puedes preguntarme directamente, por ejemplo:\n"
        "_\"Hola, cuánto me cuesta la instalación del calefón\"_",
        parse_mode="Markdown",
        reply_markup=MAIN_MENU,
    )
