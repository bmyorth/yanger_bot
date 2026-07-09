from telegram import Update
from telegram.ext import ContextTypes

from utils.matcher import contains_any
from utils.keyboards import MAIN_MENU

# Agrega aquí más formas de saludar si quieres que el bot las reconozca
GREETING_KEYWORDS = [
    "hola", "buenas", "buen dia", "buenos dias", "buenas tardes",
    "buenas noches", "hey", "que tal", "saludos", "hi", "hello",
]

GREETING_RESPONSE = (
    "¡Hola! 👋 Bienvenido/a.\n\n"
    "Puedo ayudarte con:\n"
    "📦 /productos - Ver nuestro catálogo\n"
    "🔧 /servicios - Ver nuestros servicios\n\n"
    "También puedes preguntarme directamente, por ejemplo:\n"
    "_\"Cuánto me cuesta la instalación de [producto]\"_"
)


async def handle_greeting(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """
    Devuelve True si el mensaje era un saludo y ya fue respondido.
    Devuelve False si no era un saludo (así el bot sigue buscando qué hacer).
    """
    text = update.message.text or ""
    if contains_any(text, GREETING_KEYWORDS):
        await update.message.reply_text(
            GREETING_RESPONSE, parse_mode="Markdown", reply_markup=MAIN_MENU
        )
        return True
    return False
