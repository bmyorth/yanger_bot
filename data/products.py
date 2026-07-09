"""
Catálogo de productos.

Para agregar un producto nuevo, copia uno de los diccionarios de abajo
y modifica sus valores. No necesitas tocar ningún otro archivo del proyecto.

Campos:
- id: identificador único interno (sin espacios)
- name: nombre que se muestra al usuario
- description: descripción corta
- price: precio (número, sin símbolo de moneda)
- keywords: palabras que el bot reconocerá para identificar este producto
            cuando alguien pregunte por precio/instalación en un mensaje libre
- image_url: URL pública de una imagen. Si no tienes una, pon None y el
             bot enviará solo el texto.
"""

PRODUCTS = [
    {
        "id": "aire_split_3000",
        "name": "Aire Acondicionado Split 3000W",
        "description": "Ideal para ambientes de hasta 25m². Bajo consumo eléctrico y modo eco.",
        "price": 450.00,
        "keywords": ["aire acondicionado", "split", "aire split", "ac 3000", "aire"],
        "image_url": "https://images.unsplash.com/photo-1631545806609-56b28e3d4a2e?w=600",
    },
    {
        "id": "calefon_gas_14l",
        "name": "Calefón a Gas 14L",
        "description": "Calentador de agua instantáneo, ideal para viviendas de 1-2 baños.",
        "price": 220.00,
        "keywords": ["calefon", "calefón", "calentador de agua", "termotanque"],
        "image_url": "https://images.unsplash.com/photo-1620626011761-996317b8d101?w=600",
    },
    {
        "id": "camara_seguridad_wifi",
        "name": "Cámara de Seguridad WiFi 1080p",
        "description": "Visión nocturna, detección de movimiento y grabación en la nube.",
        "price": 65.00,
        "keywords": ["camara", "cámara", "camara de seguridad", "cctv", "camaras"],
        "image_url": "https://images.unsplash.com/photo-1558002038-1055907df827?w=600",
    },
]
