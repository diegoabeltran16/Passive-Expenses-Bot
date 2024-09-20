# Importa los módulos necesarios de discord.ext para crear comandos y la utilidad de base de datos para listar gastos.
from discord.ext import commands
from utils.db import list_expenses  # Importe la función que recupera la lista de gastos de la base de datos.

# Definir una clase Cog para manejar el comando "list_expenses".
class ListExpenses(commands.Cog):
    """
    Un Cog que se encarga de listar todos los gastos almacenados en la base de datos SQLite.

    Atributos:
    -----------
    bot : commands.Bot
        La instancia del bot de Discord a la que se añade este Cog.

    Metodos:
    --------
    list_expenses(ctx):
        Recupera de la base de datos una lista de todos los gastos almacenados y los muestra en el canal.
    """

    def __init__(self, bot):
        """
        Constructor que inicializa la instancia del bot.

        Parametros:
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
        Canal de discord. Si no se encuentran gastos, el bot informa al usuario de que no hay gastos registrados.

        Parametros:
        -----------
        ctx : commands.Context
            El contexto en el que se está invocando el comando, utilizado para interactuar con el usuario y el canal.

        Comportamiento:
        ---------
        - El bot llama a la función `list_expenses()` para recuperar todos los gastos de la base de datos.
        - Si no se encuentran gastos, envía un mensaje indicando "No se han encontrado gastos".
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
        # Obtenga la lista de gastos de la base de datos utilizando la función de utilidad db.
        expenses = list_expenses()

        # Si no se encuentran gastos, notifíqueselo al usuario.
        if not expenses:
            await ctx.send("No expenses found.")
            return

        # Prepare el mensaje que enumera todos los gastos.
        message = "Here are your expenses:\n"
        for expense in expenses:
            message += f"ID: {expense[0]}, Amount: {expense[1]}, Description: {expense[2]}, Date Added: {expense[3]}\n"
        
        # Envía la lista de gastos formateada al canal.
        await ctx.send(message)

# Función de configuración asíncrona para añadir el Cog al bot.
async def setup(bot):
    """
    Añade el Cog ListExpenses al bot.

    Parametros:
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
