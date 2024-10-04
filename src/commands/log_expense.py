# Importa los módulos necesarios
from discord.ext import commands
from src.utils.lang import translate  # Importa la funcionalidad de traducción
from utils import db  # Importa las funciones para interactuar con la base de datos
from src.utils.shared import user_language  # Importa el diccionario que almacena el idioma preferido de los usuarios
from src.utils.db import connect_db

import yaml

# Carga la configuración desde el archivo config.yaml
with open("config/config.yaml", 'r') as config_file:
    config = yaml.safe_load(config_file)

# Define una clase Cog para manejar el comando "log_expense"
class LogExpense(commands.Cog):
    """
    Un Cog que gestiona el registro de gastos en la base de datos SQLite.

    Atributos:
    ----------
    bot : commands.Bot
        La instancia del bot de Discord al que se añade este Cog.

    Métodos:
    --------
    log_expense(ctx, amount: float, description: str):
        Comando que registra un nuevo gasto en la base de datos SQLite y confirma la acción al usuario.
    """

    def __init__(self, bot):
        """
        Constructor que inicializa la instancia del bot.

        Parámetros:
        -----------
        bot : commands.Bot
            La instancia del bot que utilizará este Cog.
        """
        self.bot = bot

    @commands.command(name='log_expense')
    async def log_expense(self, ctx, amount: float, description: str):
        """
        Comando que registra un nuevo gasto en la base de datos SQLite.

        Este comando permite a los usuarios registrar un gasto proporcionando una cantidad y una descripción. 
        El gasto se almacena en la base de datos y el bot confirma la acción enviando un mensaje en el canal, 
        utilizando el idioma preferido del usuario.

        Parámetros:
        -----------
        ctx : commands.Context
            El contexto en el que se invoca el comando, utilizado para interactuar con el usuario y el canal.
        amount : float
            La cantidad de dinero gastada, proporcionada por el usuario.
        description : str
            La descripción del gasto, proporcionada por el usuario.

        Comportamiento:
        ---------------
        - El bot almacena el gasto en la base de datos SQLite llamando a la función `db.add_expense()`.
        - Utiliza la función `translate()` para generar un mensaje de confirmación en el idioma preferido del usuario.
        - Envía el mensaje de confirmación al canal de Discord.

        Ejemplo de uso:
        ---------------
        El usuario escribe el siguiente comando en Discord:
        !log_expense 50.0 "Compra de alimentos"
        
        El bot registra el gasto y responde (en el idioma configurado):
        "Gasto registrado con ID 1: 50.0 por Compra de alimentos"
        """
        # Recupera el idioma preferido del usuario o establece el inglés como predeterminado
        user_id = ctx.author.id
        language = user_language.get(ctx.author.id, config.get("default_language", "en"))

        # Mensaje de depuración para confirmar el idioma obtenido
        print(f"User {user_id} is using language: {language}")

        # Añade el gasto a la base de datos SQLite
        expense_id = db.add_expense(amount, description)

        # Utiliza la función de traducción para generar una respuesta en el idioma correspondiente
        response = translate("expense_logged", language, id=expense_id, amount=amount, description=description)

        # Envía el mensaje de confirmación al canal de Discord
        await ctx.send(response)

# Función asíncrona para añadir el Cog al bot
async def setup(bot):
    """
    Añade el LogExpense Cog al bot.

    Parámetros:
    -----------
    bot : commands.Bot
        La instancia del bot al que se añade este Cog.

    Comportamiento:
    ---------------
    - Esta función es necesaria para añadir el Cog al bot de forma asíncrona.
    - Asegura que el Cog está listo y puede responder al comando 'log_expense'.

    Ejemplo de uso:
    ---------------
    Esta función se llama normalmente cuando el bot se está inicializando para cargar la funcionalidad de este comando.
    """
    await bot.add_cog(LogExpense(bot))  # Espera a que el Cog sea añadido a la instancia del bot
