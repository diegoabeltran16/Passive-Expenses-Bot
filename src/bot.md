# bot

## Descripción general

## Codigo

```
# Importa los módulos necesarios de los paquetes discord y yaml.
import discord
from discord.ext import commands
from commands.set_language import SetLanguage  # Importa el Cog para configurar el idioma
from utils.lang import translate  # Importa la función de traducción
from utils.shared import user_language  # Importa el diccionario compartido de preferencias de idioma

import yaml

# Cargar la configuración desde el archivo config.yaml
with open("config/config.yaml", 'r') as config_file:
    config = yaml.safe_load(config_file)

# Habilita intents para permitir que el bot gestione eventos como mensajes e interacciones con los usuarios.
intents = discord.Intents.default()
intents.messages = True  # Permitir que el bot lea y responda a los mensajes.
intents.message_content = True  # Habilita la intención de contenido de mensaje para acceder al contenido de texto de los mensajes.

# Inicializa la instancia del bot con el prefijo y los intents cargados desde el archivo de configuración.
bot = commands.Bot(command_prefix=config['bot']['prefix'], intents=intents)

@bot.event
async def on_ready():
    """
    Evento que se activa cuando el bot se conecta con éxito a Discord.

    Esta función se llama cuando el bot termina de iniciar sesión en Discord y establece una conexión. 
    Confirma que el bot está listo e imprime un mensaje con el nombre de usuario del bot en la consola.

    Ejemplo de salida:
    ---------------
    Conectado como Passive Expenses Bot
    """
    print(f'Logged in as {bot.user.name}')  # Confirmar el inicio de sesión del bot con su nombre

# Función asíncrona para cargar extensiones de comandos dinámicamente.
async def load_extensions():
    """
    Carga asíncrona de extensiones (módulos de comandos).

    Esta función carga dinámicamente una lista de extensiones predefinidas (comandos) que manejan varias 
    funcionalidades como registrar gastos, borrar gastos, listar gastos, actualizar gastos y configurar el idioma del usuario.

    Extensiones cargadas:
    ------------------
    1. log_expense - Registra nuevos gastos en el sistema.
    2. delete_expense - Elimina un gasto existente por ID.
    3. list_expenses - Lista todos los gastos almacenados en la base de datos.
    4. update_expense - Actualiza un gasto existente modificando el importe o la descripción.
    5. set_language - Permite a los usuarios configurar su idioma preferido para las respuestas del bot.

    Para cada extensión, el bot intenta cargarla y, en caso de fallo, se imprime un mensaje de error.

    Ejemplo de salida:
    ---------------
    Loaded extension commands.log_expense
    Loaded extension commands.delete_expense
    Failed to load extension commands.update_expense. Error: <error_message>
    """
    extensions = [
        'commands.log_expense',
        'commands.delete_expense',
        'commands.list_expenses',
        'commands.update_expense',
        'commands.set_language'  # Incluye la extensión para set_language
    ]

    for extension in extensions:
        try:
            # Intente cargar cada extensión de comando.
            await bot.load_extension(extension)
            print(f"Loaded extension {extension}")
        except Exception as e:
            # Si la carga falla, imprima el error.
            print(f"Failed to load extension {extension}. Error: {e}")

# Redefine el evento on_ready para cargar extensiones después de que el bot esté listo.
@bot.event
async def on_ready():
    """
    Evento que se activa cuando el bot se conecta con éxito a Discord.

    Esta función es llamada cuando el bot está listo, similar al evento anterior on_ready.
    Sin embargo, también llama a la función `load_extensions()` para asegurarse de que todas las extensiones de comandos
    se cargan cuando se inicia el bot.

    Ejemplo de salida:
    ---------------
    Logged in as Passive Expenses Bot
    Loaded extension commands.log_expense
    Loaded extension commands.delete_expense
    """
    print(f'Logged in as {bot.user.name}')
    await load_extensions()  # Carga todas las extensiones de comandos después de que el bot esté listo.

# Define un simple comando ping para probar si el bot responde.
@bot.command()
async def ping(ctx):
    """
    Un simple comando ping para verificar la funcionalidad del bot.

    Cuando el usuario escribe `!ping` en el chat, el bot responde con "¡Pong!".
    Este comando es útil para confirmar que el bot está en línea y es capaz de responder a los comandos.

    Parámetros:
    -----------
    ctx : commands.Context
        El contexto en el que se invoca el comando, utilizado para interactuar con el emisor del mensaje.

    Ejemplo de uso:
    --------------
    El usuario escribe `!ping` en el chat, y el bot responde con:
    Pong!
    """
    await ctx.send("Pong!")  # Responde con "¡Pong!" para verificar la capacidad de respuesta del bot.

# Función de configuración asíncrona para asegurar que el Cog SetLanguage se carga correctamente
async def setup(bot):
    """
    Configuración asíncrona para añadir el Cog SetLanguage al bot.

    Esta función asegura que el Cog SetLanguage esté cargado en el bot. 
    Verifica si ya está cargado, y si no, lo añade.

    Parámetros:
    -----------
    bot : commands.Bot
        La instancia del bot a la que se añade el Cog SetLanguage.

    Ejemplo de uso:
    --------------
    Esta función se llama normalmente al iniciar el bot para cargar la funcionalidad de este comando.
    """
    if not bot.get_cog("SetLanguage"):
        await bot.add_cog(SetLanguage(bot))
        print("SetLanguage Cog loaded successfully")
    else:
        print("SetLanguage Cog already loaded, skipping.")

# Ejecuta el bot con el token proporcionado en el archivo de configuración.
bot.run(config['bot']['token'])

```

## PseudoCodigo

```
INICIO

IMPORTAR los módulos necesarios:
    - discord y commands de discord.ext para manejar el bot y sus comandos
    - SetLanguage de commands.set_language para configurar la funcionalidad multilingüe
    - translate de utils.lang para traducir los mensajes
    - user_language de utils.shared para acceder a las preferencias de idioma de los usuarios
    - yaml para cargar la configuración

CARGAR la configuración desde el archivo config.yaml
    ABRIR el archivo config.yaml
    CARGAR la configuración en la variable 'config'

HABILITAR intents para el bot:
    - Habilitar intents para permitir que el bot lea y responda a los mensajes de Discord

INICIALIZAR el bot con el prefijo de comando especificado en la configuración y con los intents habilitados

DEFINIR el evento on_ready:
    - IMPRIMIR un mensaje que confirma que el bot ha iniciado sesión correctamente

DEFINIR la función asíncrona load_extensions():
    - CREAR una lista de extensiones que incluye los comandos log_expense, delete_expense, list_expenses, update_expense y set_language
    - PARA cada extensión en la lista:
        - INTENTAR cargar la extensión
            - IMPRIMIR un mensaje de éxito si la extensión se carga correctamente
        - SI ocurre un error, IMPRIMIR un mensaje de error con los detalles

REDEFINIR el evento on_ready para incluir la carga de extensiones:
    - IMPRIMIR un mensaje que indica que el bot ha iniciado sesión correctamente
    - LLAMAR a load_extensions() para cargar todas las extensiones de comandos

DEFINIR el comando ping:
    - CUANDO el usuario escribe `!ping` en el chat, el bot responde con "¡Pong!"

DEFINIR la función asíncrona setup(bot):
    - VERIFICAR si el Cog SetLanguage no está cargado en el bot
        - AÑADIR el Cog SetLanguage al bot y mostrar un mensaje de confirmación
    - SI el Cog ya está cargado, mostrar un mensaje indicando que se omitió

EJECUTAR el bot utilizando el token proporcionado en el archivo de configuración

FIN

```