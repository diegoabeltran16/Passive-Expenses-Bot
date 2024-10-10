# Importa los módulos necesarios de los paquetes discord y yaml.
import discord
from discord.ext import commands
from src.commands.set_language import SetLanguage  # Asegura que el path sea correcto para el Cog
from src.utils.lang import translate  # Importa la función de traducción
from src.utils.shared import user_language  # Importa el diccionario compartido de preferencias de idioma

import yaml

# Cargar la configuración desde el archivo config.yaml
with open("src/config/config.yaml", 'r') as config_file:
    config = yaml.safe_load(config_file)

# Habilita intents para permitir que el bot gestione eventos como mensajes e interacciones con los usuarios.
intents = discord.Intents.default()
intents.messages = True  # Permitir que el bot lea y responda a los mensajes.
intents.message_content = True  # Habilita la intención de contenido de mensaje para acceder al contenido de texto de los mensajes.

# Inicializa la instancia del bot con el prefijo y los intents cargados desde el archivo de configuración.
bot = commands.Bot(command_prefix=config['bot']['prefix'], intents=intents)

# Función asíncrona para cargar extensiones de comandos dinámicamente.
async def load_extensions():
    """
    Carga asíncrona de extensiones (módulos de comandos).
    """
    extensions = [
        'src.commands.log_expense',
        'src.commands.delete_expense',
        'src.commands.list_expenses',
        'src.commands.update_expense',
        'src.commands.set_language'  # Asegura el path correcto para set_language
    ]

    for extension in extensions:
        try:
            # Intente cargar cada extensión de comando.
            await bot.load_extension(extension)
            print(f"Loaded extension {extension}")
        except Exception as e:
            # Si la carga falla, imprima el error.
            print(f"Failed to load extension {extension}. Error: {e}")

@bot.event
async def on_ready():
    """
    Evento que se activa cuando el bot se conecta con éxito a Discord.
    """
    print(f'Logged in as {bot.user.name}')
    await load_extensions()  # Carga todas las extensiones de comandos después de que el bot esté listo.

# Define un simple comando ping para probar si el bot responde.
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")  # Responde con "¡Pong!" para verificar la capacidad de respuesta del bot.

# Ejecuta el bot con el token proporcionado en el archivo de configuración.
bot.run(config['bot']['token'])
