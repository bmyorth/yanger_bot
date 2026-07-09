"""
Teclados (botones) que se muestran al usuario.
"""

from telegram import ReplyKeyboardMarkup

MAIN_MENU = ReplyKeyboardMarkup(
    [["📦 Productos", "🔧 Servicios"]],
    resize_keyboard=True,
)
