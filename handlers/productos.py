from telegram import Update
from telegram.ext import ContextTypes

from data.products import PRODUCTS


async def productos_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not PRODUCTS:
        await update.message.reply_text("Aún no hay productos cargados.")
        return

    await update.message.reply_text("📦 Este es nuestro catálogo de productos:")

    for product in PRODUCTS:
        caption = (
            f"*{product['name']}*\n"
            f"{product['description']}\n\n"
            f"💰 Precio: ${product['price']:.2f}"
        )
        image_url = product.get("image_url")

        if image_url:
            try:
                await update.message.reply_photo(
                    photo=image_url,
                    caption=caption,
                    parse_mode="Markdown",
                )
                continue
            except Exception:
                # Si la imagen falla (URL rota, sin internet, etc.)
                # mandamos igual la info en texto para no cortar el flujo.
                pass

        await update.message.reply_text(caption, parse_mode="Markdown")
