# Importa los módulos necesarios de discord.ext para crear comandos y la utilidad db para interactuar con la base de datos SQLite.
from discord.ext import commands  
from utils import db  # Importe el módulo db donde se encuentran sus funciones de base de datos


# Definir una clase Cog para manejar el comando "log_expense".
class LogExpense(commands.Cog):
    """
    Un Cog que gestiona el registro de gastos en la base de datos SQLite.

    Atributos:
    -----------
    bot : commands.Bot
        La instancia del bot de Discord a la que se añade este Cog.

    Metodos:
    --------
    log_expense(ctx, amount: float, description: str):
        Registra un nuevo gasto en la base de datos y confirma la acción enviando un mensaje en el canal.
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

    @commands.command(name='log_expense')
    async def log_expense(self, ctx, amount: float, description: str):
        """
        Un comando que registra un nuevo gasto en la base de datos SQLite.

        Este comando permite a los usuarios registrar gastos proporcionando un importe y una descripción.
        El gasto se almacena en la base de datos, y el bot confirma la acción enviando un mensaje de vuelta al canal.

        Parametros:
        -----------
        ctx : commands.Context
            El contexto en el que se está invocando el comando, utilizado para interactuar con el usuario y el canal.
        amount : float
            La cantidad de dinero gastada, facilitada por el usuario.
        description : str
            Descripción del gasto, facilitada por el usuario.

        Comportamiento:
        ---------
        - El bot almacena el gasto en la base de datos SQLite llamando a la función `db.add_expense()`.
        - Tras registrar correctamente el gasto, el bot envía un mensaje de confirmación al canal,
          incluyendo el ID del gasto, el importe y la descripción.

        Ejemplo de uso:
        --------------
        El usuario escribe el siguiente comando en Discord:
        !log_expense 50.0 "Groceries"
        
        El bot registra el gasto con ID 1 y responde:
        "Expense logged with ID 1: 50.0 for Groceries"
        """
        # Añadir el gasto a la base de datos SQLite
        expense_id = db.add_expense(amount, description)

        # Confirme que el gasto se ha registrado enviando un mensaje al canal de Discordia
        await ctx.send(f'Expense logged with ID {expense_id}: {amount} for {description}')

# Función de configuración asíncrona para añadir el Cog al bot
async def setup(bot):
    """
    Añade el LogExpense Cog al bot.

    Parametros:
    -----------
    bot : commands.Bot
        La instancia de bot a la que se añade este Cog.

    Comportamiento:
    ---------
    - Esta función es necesaria para añadir el Cog al bot de forma asíncrona.
    - Asegura que el Cog está listo y puede responder al comando 'log_expense'.

    Ejemplo de uso:
    --------------
    Esta función se llama normalmente cuando el bot se está inicializando para cargar la funcionalidad de este comando.
    """
    await bot.add_cog(LogExpense(bot))  # Espera la llamada add_cog para añadir este Cog a la instancia del bot.
