# Importa los módulos necesarios del paquete discord.ext para crear comandos bot y la utilidad de base de datos.
from discord.ext import commands
from utils.db import update_expense  # Importar la función para actualizar el gasto en la base de datos
from src.utils.lang import translate  # Importar la función de traducción para respuestas multilingües
from src.utils.shared import user_language  # Importar la variable que guarda las preferencias de idioma del usuario
from src.utils.db import connect_db

import yaml

# Cargar la configuración desde el archivo config.yaml
with open("config/config.yaml", 'r') as config_file:
    config = yaml.safe_load(config_file)

# Definir una clase Cog para manejar el comando "update_expense".
class UpdateExpense(commands.Cog):
    """
    Un Cog que se encarga de actualizar los gastos existentes en la base de datos.

    Atributos:
    -----------
    bot : commands.Bot
        La instancia del bot de Discord a la que se añade este Cog.
    
    Métodos:
    --------
    update_expense(ctx, expense_id: int, new_amount: float, new_description: str):
        Actualiza un gasto existente en la base de datos a partir de la información introducida por el usuario.
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

    @commands.command(name='update_expense')
    async def update_expense(self, ctx, expense_id: int, new_amount: float, new_description: str):
        """
        Un comando que actualiza un gasto existente en la base de datos SQLite.

        Este comando permite a los usuarios modificar el importe y la descripción de un gasto específico identificado por 
        su ID de gasto.

        Parámetros:
        -----------
        ctx : commands.Context
            El contexto en el que se está invocando el comando, utilizado para enviar respuestas al usuario.
        expense_id : int
            El ID único del gasto a actualizar.
        new_amount : float
            El nuevo importe que se asignará al gasto especificado.
        new_description : str
            La nueva descripción del gasto.

        Comportamiento:
        ---------
        - Intenta actualizar el gasto en la base de datos con el nuevo importe y descripción dados. 
        - Si tiene éxito, envía un mensaje de confirmación al usuario en su idioma preferido. 
        - Si se produce un error (por ejemplo, un ID de gasto no válido), envía un mensaje de error traducido.
        
        Ejemplo de uso:
        --------------
        El usuario escribe el siguiente comando en Discord:
        !update_expense 3 150.0 "Groceries for the week"
        Esto actualizará el gasto con ID 3 para que tenga un importe de 150,0 y una descripción de "Groceries for the week".
        """
        try:
            # Obtener el idioma preferido del usuario o el predeterminado de la configuración
            user_id = ctx.author.id
            language = user_language.get(user_id, config.get("default_language", "en"))

            # Imprimir el idioma seleccionado para fines de depuración
            print(f"User {user_id} is using language: {language}")

            # Intentar actualizar el gasto en la base de datos
            update_expense(expense_id, new_amount, new_description)
            
            # Generar el mensaje de confirmación traducido
            response = translate("expense_updated", language, id=expense_id, amount=new_amount, description=new_description)
            
            # Enviar mensaje de confirmación al usuario
            await ctx.send(response)
        except Exception as e:
            # En caso de error, enviar un mensaje de error traducido
            error_response = translate("update_failed", language, error=str(e))
            await ctx.send(error_response)

# Función de configuración asíncrona para añadir el Cog al bot
async def setup(bot):
    """
    Añade el Cog UpdateExpense al bot.

    Parámetros:
    -----------
    bot : commands.Bot
        La instancia de bot a la que se añade este Cog.

    Comportamiento:
    ---------
    - Esta función es necesaria para añadir el Cog al bot de forma asíncrona. 
    - Asegura que el Cog está listo y puede responder al comando 'update_expense'.

    Ejemplo de uso:
    --------------
    Esta función se llama normalmente cuando el bot se está inicializando.
    """
    await bot.add_cog(UpdateExpense(bot))  # Añade el Cog al bot de forma asíncrona.

