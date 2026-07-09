from telegram import Update
from telegram.ext import ContextTypes

from data.products import PRODUCTS
from data.services import SERVICES
from utils.matcher import contains_any, find_product, find_service

# Frases que indican que el usuario quiere saber un precio/costo
PRICE_INTENT_KEYWORDS = [
    "cuanto cuesta", "cuánto cuesta", "cuanto sale", "cuanto vale",
    "precio", "cotizar", "cotizacion", "cotización", "presupuesto", "costo",
]

# Palabras que indican que además quiere instalación
INSTALLATION_KEYWORDS = ["instalacion", "instalación", "instalar"]


async def maybe_answer_pricing(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """
    Si el mensaje parece una pregunta de precio/instalación, responde con un
    cálculo aproximado y devuelve True. Si no aplica, devuelve False para que
    el bot siga probando otras respuestas (saludo, etc.).
    """
    text = update.message.text or ""

    quiere_precio = contains_any(text, PRICE_INTENT_KEYWORDS)
    quiere_instalacion = contains_any(text, INSTALLATION_KEYWORDS)

    if not quiere_precio and not quiere_instalacion:
        return False

    product = find_product(text, PRODUCTS)
    service = find_service(text, SERVICES)

    # Si mencionó "instalación" pero no un servicio específico,
    # usamos el servicio marcado como instalación por defecto.
    if not service and quiere_instalacion:
        service = next((s for s in SERVICES if s.get("default_installation")), None)

    # No identificamos ningún producto en el mensaje
    if not product:
        await update.message.reply_text(
            "Puedo darte un cálculo aproximado 🙂\n"
            "¿Podrías decirme el nombre del producto? Puedes ver el listado "
            "completo con /productos."
        )
        return True

    # Identificamos producto pero no pidió instalación / no hay servicio
    if not service:
        await update.message.reply_text(
            f"El *{product['name']}* cuesta aproximadamente ${product['price']:.2f}.\n"
            "Si también necesitas instalación, dime y te doy el total con ese costo incluido.",
            parse_mode="Markdown",
        )
        return True

    # Tenemos producto + servicio -> calculamos el total
    total = product["price"] + service["price"]
    await update.message.reply_text(
        f"📦 *{product['name']}*: ${product['price']:.2f}\n"
        f"🔧 *{service['name']}*: ${service['price']:.2f}\n"
        f"➖➖➖➖➖➖➖➖\n"
        f"💰 *Total aproximado*: ${total:.2f}\n\n"
        f"_Este es un cálculo estimado. El precio final puede variar según "
        f"tu ubicación y las condiciones del lugar de instalación._",
        parse_mode="Markdown",
    )
    return True
