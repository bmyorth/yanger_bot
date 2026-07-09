# Bot de Telegram - Proyecto base

Bot con comandos `/productos` y `/servicios`, respuesta a saludos, y un
cálculo aproximado de precio cuando alguien pregunta algo como:
*"Hola, cuánto me cuesta la instalación del calefón"*.

## Estructura del proyecto

```
telegram_bot_project/
├── bot.py                  ← Punto de entrada (correr este archivo)
├── config.py                ← Carga el token desde .env
├── requirements.txt         ← Dependencias
├── .env.example              ← Plantilla para tu token
├── data/
│   ├── products.py          ← EDITA AQUÍ tus productos
│   └── services.py          ← EDITA AQUÍ tus servicios
├── handlers/
│   ├── start.py              ← Comando /start
│   ├── productos.py          ← Comando /productos
│   ├── servicios.py          ← Comando /servicios
│   ├── greetings.py          ← Respuestas a saludos
│   └── pricing.py            ← Cálculo de precio + instalación
└── utils/
    ├── matcher.py             ← Funciones para reconocer texto
    └── keyboards.py           ← Botones del menú
```

Cada tipo de respuesta vive en su propio archivo. Para agregar algo nuevo
casi nunca necesitas tocar `bot.py`.

---

## Paso a paso en Windows

### 1. Instalar Python

1. Ve a https://www.python.org/downloads/
2. Descarga la última versión de Python 3 (3.11 o superior).
3. Al instalar, **marca la casilla "Add Python to PATH"** (muy importante, es
   el error más común). Luego clic en "Install Now".
4. Verifica que se instaló correctamente. Abre el **Símbolo del sistema**
   (busca "cmd" en el menú Inicio) y escribe:
   ```
   python --version
   ```
   Debería mostrarte algo como `Python 3.12.x`.

### 2. Descargar/descomprimir el proyecto

Descomprime el .zip del proyecto en una carpeta, por ejemplo:
`C:\Users\TuUsuario\telegram_bot_project`

### 3. Abrir una terminal en la carpeta del proyecto

Dentro del explorador de Windows, abre la carpeta del proyecto, haz clic en
la barra de direcciones, escribe `cmd` y presiona Enter. Se abrirá una
terminal ya ubicada en esa carpeta.

### 4. Crear un entorno virtual (recomendado)

Esto evita conflictos con otras cosas instaladas en tu PC:
```
python -m venv venv
venv\Scripts\activate
```
Vas a ver que la línea de la terminal ahora empieza con `(venv)`.

*(Cada vez que vuelvas a trabajar en el proyecto, deberás activar el
entorno de nuevo con `venv\Scripts\activate` desde esta carpeta)*

### 5. Instalar las dependencias

```
pip install -r requirements.txt
```

### 6. Crear tu bot en Telegram y obtener el token

1. Abre Telegram (móvil o desktop) y busca el usuario **@BotFather**.
2. Envíale `/newbot`.
3. Te pedirá un nombre visible (ej. "Mi Negocio Bot") y un username que
   debe terminar en "bot" (ej. `mi_negocio_bot`).
4. BotFather te dará un **token**, algo como:
   ```
   7123456789:AAHxK3f...abcdefg
   ```

### 7. Configurar el token en el proyecto

1. En la carpeta del proyecto, copia el archivo `.env.example` y
   renombra la copia a `.env` (así, tal cual, con el punto adelante).
2. Ábrelo con el Bloc de notas y reemplaza el texto de ejemplo por tu
   token real:
   ```
   TELEGRAM_BOT_TOKEN=7123456789:AAHxK3f...abcdefg
   ```
3. Guarda el archivo.

### 8. Correr el bot

Con el entorno virtual activado (ves `(venv)` en la terminal):
```
python bot.py
```
Si todo está bien verás:
```
Bot iniciado correctamente. Presiona Ctrl+C para detenerlo.
```
Ahora abre Telegram, busca tu bot por el username que le pusiste, y
escríbele `/start`.

Para detenerlo, vuelve a la terminal y presiona `Ctrl + C`.

---

## Solución de problemas al desplegar (Railway u otros)

**Error: `AttributeError: 'Application' object has no attribute '_Application__stop_running_marker' and no __dict__ for setting new attributes`**

Esto pasa cuando el servidor usa una versión de Python (por ejemplo 3.13) más nueva que la que soportaba tu versión fijada de `python-telegram-bot`. Se soluciona así:
1. Verifica que `requirements.txt` tenga `python-telegram-bot==22.8` (o una versión igual o más reciente).
2. Este proyecto ya incluye un archivo `.python-version` con `3.12` para que Railway use esa versión de Python de forma consistente.
3. En Railway, vuelve a desplegar forzando una build limpia (sin caché): **Deployments → ⋮ → Redeploy**.

## Cómo personalizar

### Agregar/editar productos
Abre `data/products.py` y copia un bloque como este, cambiando los valores:
```python
{
    "id": "mi_producto",
    "name": "Nombre del producto",
    "description": "Descripción corta",
    "price": 100.00,
    "keywords": ["palabra1", "palabra2"],  # formas en que la gente lo puede nombrar
    "image_url": "https://url-de-tu-imagen.jpg",  # o None si no tienes
},
```

### Agregar/editar servicios
Igual que productos, pero en `data/services.py`. Si marcas
`"default_installation": True` en un servicio, ese será el que se use
cuando alguien mencione "instalación" sin especificar cuál.

### Agregar nuevas palabras de saludo
Edita la lista `GREETING_KEYWORDS` en `handlers/greetings.py`.

### Agregar un comando nuevo (ej. /contacto)
1. Crea `handlers/contacto.py` con una función `async def contacto_command(update, context): ...`
2. En `bot.py`, impórtala y agrega la línea:
   ```python
   app.add_handler(CommandHandler("contacto", contacto_command))
   ```

---

## Notas importantes

- **Imágenes**: las URLs de ejemplo en `products.py` son solo demostrativas.
  Reemplázalas por imágenes tuyas (puedes subirlas a Imgur, tu web, Google
  Drive con enlace público, etc.). Si una imagen falla, el bot envía el
  texto igual, no se rompe.
- **Mantener el bot corriendo 24/7**: mientras tengas la terminal abierta
  con `python bot.py` corriendo, el bot responde. Si cierras la terminal,
  se apaga. Para que esté siempre disponible (no solo en tu PC prendida),
  más adelante puedes subir este mismo código a un servicio como Railway
  o Render (ambos tienen planes gratuitos/económicos).
- **El cálculo de precios es aproximado**: el bot busca coincidencias de
  palabras clave, no es inteligencia artificial. Si quieres respuestas más
  flexibles y naturales, se puede conectar más adelante a un modelo de
  lenguaje (puedo ayudarte con eso si lo necesitas).
