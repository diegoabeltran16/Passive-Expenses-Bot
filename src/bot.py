# Importa los módulos necesarios de los paquetes discord y yaml.
import discord
from discord.ext import commands
import yaml

# Cargar la configuración desde el archivo config.yaml
with open("config/config.yaml", 'r') as config_file:
    config = yaml.safe_load(config_file)

# Habilita intents para permitir que el bot gestione eventos como mensajes e interacciones con los usuarios.
intents = discord.Intents.default()
intents.messages = True  # Permitir que el bot lea y responda a los mensajes.
intents.message_content = True  # Habilite la intención de contenido de mensaje para acceder al contenido de texto de los mensajes.

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
    funcionalidades como registrar gastos, borrar gastos, listar gastos y actualizar gastos.

    Extensiones cargadas:
    ------------------
    1. log_expense - Registra nuevos gastos en el sistema.
    2. delete_expense - Elimina un gasto existente por ID.
    3. list_expenses - Lista todos los gastos almacenados en la base de datos.
    4. update_expense - Actualiza un gasto existente modificando el importe o la descripción.

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
        'commands.update_expense'
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

    Parametros:
    -----------
    ctx : commands.Context
        El contexto en el que se invoca el comando, utilizado para interactuar con el emisor del mensaje.

    Ejemplo de uso:
    --------------
    El usuario escribe `!ping` en el chat, y el bot responde con:
    Pong!
    """
    await ctx.send("Pong!")  # Responde con "¡Pong!" para verificar la capacidad de respuesta del bot.

# Ejecuta el bot con el token proporcionado en el archivo de configuración.
bot.run(config['bot']['token'])
