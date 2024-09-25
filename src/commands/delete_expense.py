# Importar los módulos necesarios de discord.ext para crear comandos y la utilidad db para eliminar gastos.
from discord.ext import commands
from utils.lang import translate  # Importar el módulo de traducción para proporcionar respuestas multilingües
from utils import db  # Importar el módulo db donde se encuentran sus funciones de base de datos.
from utils.shared import user_language  # Importar el diccionario user_language para acceder a las preferencias de idioma del usuario
import yaml

# Cargar configuración desde config.yaml
with open("config/config.yaml", 'r') as config_file:
    config = yaml.safe_load(config_file)

# Definir una clase Cog para manejar el comando "delete_expense".
class DeleteExpense(commands.Cog):
    """
    Un Cog que se encarga de borrar un gasto de la base de datos SQLite.

    Atributos:
    -----------
    bot : commands.Bot
        La instancia del bot de Discord a la que se añade este Cog.

    Métodos:
    --------
    delete_expense(ctx, expense_id: int):
        Elimina un gasto por su ID de la base de datos y confirma la eliminación en el canal.
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

    @commands.command(name='delete_expense')
    async def delete_expense(self, ctx, expense_id: int):
        """
        Un comando que borra un gasto de la base de datos SQLite.

        Este comando permite a los usuarios eliminar un gasto proporcionando su ID único.
        Tras eliminar el gasto de la base de datos, el bot confirma la acción enviando
        un mensaje al canal, incluyendo el ID del gasto eliminado.

        Parámetros:
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
        # Obtener el idioma preferido del usuario, utilizando 'en' como valor predeterminado si no está configurado
        user_id = ctx.author.id
        language = user_language.get(ctx.author.id, config.get("default_language", "en"))

        # Eliminar el gasto especificado de la base de datos
        db.delete_expense(expense_id)

        # Utilizar la función de traducción para generar una respuesta en el idioma del usuario
        response = translate("expense_deleted", language, id=expense_id)

        # Enviar la respuesta traducida al canal de Discord
        await ctx.send(response)

# Función de configuración asíncrona para añadir el Cog al bot.
async def setup(bot):
    """
    Añade el Cog DeleteExpense al bot.

    Parámetros:
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
