# list_expenses

## Descripción general

## Codigo

```
# Importar los módulos necesarios
from discord.ext import commands  # Para la creación de comandos de Discord
from utils.lang import translate  # Para la función de traducción de mensajes
from utils.db import list_expenses  # Importar la función que recupera la lista de gastos de la base de datos
from utils.shared import user_language  # Importar el diccionario que almacena las preferencias de idioma de los usuarios
import yaml  # Para manejar la carga de archivos de configuración

# Cargar configuración desde config.yaml
with open("config/config.yaml", 'r') as config_file:
    config = yaml.safe_load(config_file)

# Definir una clase Cog para manejar el comando "list_expenses".
class ListExpenses(commands.Cog):
    """
    Un Cog que se encarga de listar todos los gastos almacenados en la base de datos SQLite.

    Atributos:
    -----------
    bot : commands.Bot
        La instancia del bot de Discord a la que se añade este Cog.

    Métodos:
    --------
    list_expenses(ctx):
        Recupera de la base de datos una lista de todos los gastos almacenados y los muestra en el canal.
    """

    def __init__(self, bot):
        """
        Constructor que inicializa la instancia del bot.

        Parámetros:
        -----------
        bot : commands.Bot
            La instancia del bot que usará este Cog.
        """
        self.bot = bot

    @commands.command(name='list_expenses')
    async def list_expenses(self, ctx):
        """
        Un comando que lista todos los gastos de la base de datos SQLite y los envía al canal Discord.

        Este comando recupera todos los gastos registrados y los formatea en un mensaje que se envía al
        canal de Discord. Si no se encuentran gastos, el bot informa al usuario de que no hay gastos registrados.

        Parámetros:
        -----------
        ctx : commands.Context
            El contexto en el que se está invocando el comando, utilizado para interactuar con el usuario y el canal.

        Comportamiento:
        ---------
        - El bot llama a la función `list_expenses()` para recuperar todos los gastos de la base de datos.
        - Si no se encuentran gastos, envía un mensaje indicando "No expenses found".
        - Si se encuentran gastos, formatea cada gasto en un mensaje legible (incluyendo el ID, el importe, la descripción y la fecha).
        - El bot envía la lista de gastos formateada al canal.

        Ejemplo de uso:
        --------------
        El usuario escribe el siguiente comando en Discord:
        !list_expenses
        
        Si se encuentran gastos, el bot responde con:
        "Here are your expenses:
        ID: 1, Amount: 100.0, Description: Lunch at cafe, Date Added: 2024-09-18 12:34:56
        ID: 2, Amount: 50.0, Description: Groceries, Date Added: 2024-09-18 13:40:21"

        Si no se encuentran gastos, el bot responde con:
        "No expenses found."
        """
        # Recuperar el idioma preferido del usuario o utilizar el predeterminado
        user_id = ctx.author.id
        language = user_language.get(user_id, config.get("default_language", "en"))

        # Obtener la lista de gastos de la base de datos utilizando la función de utilidad db
        expenses = list_expenses()

        # Si no se encuentran gastos, enviar el mensaje traducido correspondiente
        if not expenses:
            response = translate("no_expenses_found", language)
            await ctx.send(response)
            return

        # Utilizar la función de traducción para el encabezado de la lista de gastos
        response = translate("here_are_your_expenses", language) + "\n"
        # Agregar los detalles de cada gasto
        for expense in expenses:
            response += f"ID: {expense[0]}, Amount: {expense[1]}, Description: {expense[2]}, Date Added: {expense[3]}\n"
        
        # Enviar la lista de gastos formateada al canal
        await ctx.send(response)

# Función de configuración asíncrona para añadir el Cog al bot.
async def setup(bot):
    """
    Añade el Cog ListExpenses al bot.

    Parámetros:
    -----------
    bot : commands.Bot
        La instancia de bot a la que se añade este Cog.

    Comportamiento:
    ---------
    - Esta función es necesaria para añadir el Cog al bot de forma asíncrona.
    - Asegura que el Cog está listo y puede responder al comando 'list_expenses'.

    Ejemplo de uso:
    --------------
    Esta función se llama normalmente cuando el bot se está inicializando para cargar la funcionalidad de este comando.
    """
    await bot.add_cog(ListExpenses(bot))  # Espera la llamada add_cog para añadir este Cog a la instancia del bot.

```

## PseudoCodigo

```
INICIO

IMPORTAR los módulos necesarios:
    - commands de discord.ext para manejar comandos de Discord
    - translate de utils.lang para la funcionalidad de traducción
    - list_expenses de utils.db para recuperar la lista de gastos desde la base de datos
    - user_language de utils.shared para acceder a las preferencias de idioma de los usuarios
    - yaml para la carga de configuraciones

CARGAR la configuración desde el archivo config.yaml
    ABRIR el archivo config.yaml
    CARGAR la configuración en la variable 'config'

DEFINIR la clase ListExpenses como un "Cog" para manejar el comando de listar gastos
    MÉTODO __init__(self, bot):
        GUARDAR la instancia del bot en un atributo de la clase

    DEFINIR el método list_expenses como un comando
        RECIBIR el parámetro ctx (contexto del comando)

        OBTENER el idioma preferido del usuario
            SI el usuario tiene un idioma configurado en user_language:
                ASIGNAR ese idioma a la variable 'language'
            DE LO CONTRARIO:
                ASIGNAR el idioma predeterminado de la configuración (config) a 'language'

        LLAMAR a la función list_expenses() para obtener la lista de gastos

        SI no hay gastos:
            TRADUCIR el mensaje "no_expenses_found" usando la función translate y el idioma del usuario
            ENVIAR el mensaje traducido al canal de Discord
            TERMINAR

        CREAR un mensaje que contenga la cabecera "here_are_your_expenses" traducida al idioma del usuario

        PARA cada gasto en la lista de gastos:
            AÑADIR los detalles del gasto al mensaje (ID, Amount, Description, Date Added)

        ENVIAR el mensaje completo al canal de Discord

FUNCIÓN asíncrona setup(bot):
    AÑADIR el Cog ListExpenses al bot utilizando add_cog
    ESPERAR a que el Cog sea añadido al bot

FIN

```