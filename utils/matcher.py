"""
Funciones de ayuda para "entender" el texto que escribe el usuario.
Todo se compara en minúsculas y sin acentos para que "instalación",
"Instalacion" e "INSTALACIÓN" se reconozcan igual.
"""

import unicodedata


def normalize(text: str) -> str:
    """Pasa a minúsculas y quita acentos."""
    text = text.lower()
    text = "".join(
        c for c in unicodedata.normalize("NFD", text)
        if unicodedata.category(c) != "Mn"
    )
    return text


def contains_any(text: str, keywords: list[str]) -> bool:
    """True si el texto contiene alguna de las palabras clave."""
    norm_text = normalize(text)
    return any(normalize(kw) in norm_text for kw in keywords)


def find_product(text: str, products: list[dict]):
    """Devuelve el primer producto cuyo nombre o keywords aparezcan en el texto."""
    norm_text = normalize(text)
    for product in products:
        candidates = product.get("keywords", []) + [product["name"]]
        for kw in candidates:
            if normalize(kw) in norm_text:
                return product
    return None


def find_service(text: str, services: list[dict]):
    """Devuelve el primer servicio cuyo nombre o keywords aparezcan en el texto."""
    norm_text = normalize(text)
    for service in services:
        candidates = service.get("keywords", []) + [service["name"]]
        for kw in candidates:
            if normalize(kw) in norm_text:
                return service
    return None
