# Importa los módulos necesarios de discord.ext para crear comandos y la utilidad db para eliminar gastos.
from discord.ext import commands
from utils import db  # Importe el módulo db donde se encuentran sus funciones de base de datos.

# Definir una clase Cog para manejar el comando "delete_expense".
class DeleteExpense(commands.Cog):
    """
    Un Cog que se encarga de borrar un gasto de la base de datos SQLite.

    Atributos:
    -----------
    bot : commands.Bot
        La instancia del bot de Discord a la que se añade este Cog.

    Metodos:
    --------
    delete_expense(ctx, expense_id: int):
        Elimina un gasto por su ID de la base de datos y confirma la eliminación en el canal.
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

    @commands.command(name='delete_expense')
    async def delete_expense(self, ctx, expense_id: int):
        """
        Un comando que borra un gasto de la base de datos SQLite.

        Este comando permite a los usuarios eliminar un gasto proporcionando su ID único.
        Tras eliminar el gasto de la base de datos, el bot confirma la acción enviando
        un mensaje al canal, incluyendo el ID del gasto eliminado.

        Parametros:
        -----------
        ctx : commands.Context
            El contexto en el que se está invocando el comando, utilizado para interactuar con el usuario y el canal.
        expense_id : int
            El ID único del gasto que se va a eliminar.

        Comportamiento:
        ---------
        - El bot llama a la función `db.delete_expense()` para borrar el gasto por ID.
        - Después de eliminar correctamente el gasto, el bot envía un mensaje de confirmación al canal.

        Ejemplo de uso:
        --------------
        El usuario escribe el siguiente comando en Discord:
        !delete_expense 3
        
        Si el gasto con ID 3 existe, el bot elimina el gasto y responde:
        "Expense with ID 3 deleted."
        """
        # Llama a la función delete_expense de la base de datos para eliminar el gasto especificado.
        db.delete_expense(expense_id)

        # Confirme que el gasto se ha eliminado enviando un mensaje a la dirección canal de Discord .
        await ctx.send(f'Expense with ID {expense_id} deleted.')

# Función de configuración asíncrona para añadir el Cog al bot.
async def setup(bot):
    """
    Añade el Cog DeleteExpense al bot.

    Parameteros:
    -----------
    bot : commands.Bot
        La instancia de bot a la que se añade este Cog.

    Comportamiento:
    ---------
    - Esta función es necesaria para añadir el Cog al bot de forma asíncrona.
    - Asegura que el Cog está listo y puede responder al comando 'delete_expense'.

    Ejemplo de uso:
    --------------
    Esta función se llama normalmente cuando el bot se está inicializando para cargar la funcionalidad de este comando.
    """
    await bot.add_cog(DeleteExpense(bot))  # Espera la llamada add_cog para añadir este Cog a la instancia del bot.
