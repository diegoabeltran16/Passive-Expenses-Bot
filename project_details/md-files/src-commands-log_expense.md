# src/commands/log_expense.py

## Descripción General
Permitir a los usuarios de un bot de Discord registrar gastos de manera dinámica en una base de datos SQLite. La funcionalidad incluye la gestión de comandos que permiten a los usuarios añadir un gasto con una cantidad y descripción, y recibir una confirmación en su idioma preferido (inglés o español). El código se basa en el uso de Cogs para manejar la lógica de los comandos y asegurar que el bot sea modular y fácil de mantener.

## Pseudo Codigo

## Codigo

```
# Importa los módulos necesarios
from discord.ext import commands
from utils.lang import translate  # Importa la funcionalidad de traducción
from utils import db  # Importa las funciones para interactuar con la base de datos
from utils.shared import user_language  # Importa el diccionario que almacena el idioma preferido de los usuarios

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

```

## Pseudocodigo

```
INICIO

IMPORTAR los módulos necesarios:
    - commands de discord.ext para manejar comandos de Discord
    - translate de utils.lang para la funcionalidad de traducción
    - db de utils para la interacción con la base de datos
    - user_language de utils.shared para acceder a las preferencias de idioma de los usuarios
    - yaml para la carga de configuraciones

CARGAR la configuración desde el archivo config.yaml
    ABRIR el archivo config.yaml
    CARGAR la configuración en la variable 'config'

DEFINIR la clase LogExpense como un "Cog" para manejar el comando de registro de gastos
    MÉTODO __init__(self, bot):
        GUARDAR la instancia del bot en un atributo de la clase

    DEFINIR el método log_expense como un comando
        RECIBIR los parámetros: ctx (contexto del comando), amount (cantidad del gasto), y description (descripción del gasto)

        OBTENER el idioma preferido del usuario
            SI el usuario tiene un idioma configurado en user_language:
                ASIGNAR ese idioma a la variable 'language'
            DE LO CONTRARIO:
                ASIGNAR el idioma predeterminado de la configuración (config) a 'language'

        IMPRIMIR el idioma seleccionado para depuración

        REGISTRAR el gasto en la base de datos llamando a db.add_expense
            ALMACENAR el ID del nuevo gasto en 'expense_id'

        TRADUCIR el mensaje de confirmación utilizando la función translate
            PASAR el mensaje clave "expense_logged" y los detalles del gasto a la función translate

        ENVIAR el mensaje traducido al canal de Discord usando ctx.send

FUNCIÓN asíncrona setup(bot):
    AÑADIR el Cog LogExpense al bot utilizando add_cog
    ESPERAR a que el Cog sea añadido al bot

FIN

```