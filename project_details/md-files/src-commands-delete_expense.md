# delete_expense

## Descripción General

## Pseudo Codigo

## Codigo

```
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

```

## PseudoCodigo

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

DEFINIR la clase DeleteExpense como un "Cog" para manejar el comando de eliminar gastos
    MÉTODO __init__(self, bot):
        GUARDAR la instancia del bot en un atributo de la clase

    DEFINIR el método delete_expense como un comando
        RECIBIR los parámetros: ctx (contexto del comando) y expense_id (ID del gasto a eliminar)

        OBTENER el idioma preferido del usuario
            SI el usuario tiene un idioma configurado en user_language:
                ASIGNAR ese idioma a la variable 'language'
            DE LO CONTRARIO:
                ASIGNAR el idioma predeterminado de la configuración (config) a 'language'

        IMPRIMIR el idioma seleccionado para depuración

        LLAMAR a la función db.delete_expense para eliminar el gasto de la base de datos

        TRADUCIR el mensaje de confirmación utilizando la función translate
            PASAR el mensaje clave "expense_deleted" y el ID del gasto a la función translate

        ENVIAR el mensaje traducido al canal de Discord usando ctx.send

FUNCIÓN asíncrona setup(bot):
    AÑADIR el Cog DeleteExpense al bot utilizando add_cog
    ESPERAR a que el Cog sea añadido al bot

FIN

```