"""
Configuración general del bot.
Carga el token de Telegram desde el archivo .env (nunca lo escribas
directamente en el código para no exponerlo si compartes el proyecto).
"""

import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError(
        "No se encontró TELEGRAM_BOT_TOKEN.\n"
        "1. Copia el archivo .env.example y renómbralo a .env\n"
        "2. Pega ahí el token que te dio @BotFather en Telegram\n"
    )
