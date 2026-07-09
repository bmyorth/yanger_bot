from telegram import Update
from telegram.ext import ContextTypes

from data.services import SERVICES


async def servicios_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not SERVICES:
        await update.message.reply_text("Aún no hay servicios cargados.")
        return

    await update.message.reply_text("🔧 Estos son nuestros servicios:")

    for service in SERVICES:
        caption = (
            f"*{service['name']}*\n"
            f"{service['description']}\n\n"
            f"💰 Precio: ${service['price']:.2f}"
        )
        image_url = service.get("image_url")

        if image_url:
            try:
                await update.message.reply_photo(
                    photo=image_url,
                    caption=caption,
                    parse_mode="Markdown",
                )
                continue
            except Exception:
                pass

        await update.message.reply_text(caption, parse_mode="Markdown")
