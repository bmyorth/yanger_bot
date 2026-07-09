"""
Catálogo de servicios.

Mismo formato que products.py. El campo "default_installation" marca
cuál es el servicio de instalación "genérico" que se usa cuando el
usuario menciona "instalación" pero no se detecta un servicio más
específico.
"""

SERVICES = [
    {
        "id": "instalacion_estandar",
        "name": "Instalación estándar",
        "description": "Instalación a domicilio, incluye mano de obra y materiales menores.",
        "price": 80.00,
        "keywords": ["instalacion", "instalación", "instalar", "instalarlo", "instalarla"],
        "default_installation": True,
        "image_url": None,
    },
    {
        "id": "mantenimiento_preventivo",
        "name": "Mantenimiento preventivo",
        "description": "Revisión y limpieza general cada 6 meses.",
        "price": 40.00,
        "keywords": ["mantenimiento", "revision", "revisión", "limpieza"],
        "default_installation": False,
        "image_url": None,
    },
    {
        "id": "reparacion",
        "name": "Reparación / diagnóstico",
        "description": "Visita técnica para diagnosticar y reparar fallas.",
        "price": 50.00,
        "keywords": ["reparacion", "reparación", "arreglo", "diagnostico", "diagnóstico"],
        "default_installation": False,
        "image_url": None,
    },
]
