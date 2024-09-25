# Importa los módulos necesarios para crear comandos de Discord
from discord.ext import commands
from utils.shared import user_language  # Importa el diccionario compartido user_language

class SetLanguage(commands.Cog):
    """
    Un Cog que permite a los usuarios configurar su idioma preferido para las respuestas del bot.
    
    Atributos:
    ----------
    bot : commands.Bot
        La instancia del bot de Discord a la que se añade este Cog.
    """
    
    def __init__(self, bot):
        """
        Constructor que inicializa la instancia del bot.
        
        Parámetros:
        ----------
        bot : commands.Bot
            La instancia del bot que utilizará este Cog.
        """
        self.bot = bot

    @commands.command(name='set_language')
    async def set_language(self, ctx, language_code: str):
        """
        Comando que permite a los usuarios establecer su idioma preferido para las respuestas del bot.
        
        Parámetros:
        ----------
        ctx : commands.Context
            El contexto en el que se invoca el comando, proporciona información sobre cómo y dónde se utilizó el comando.
        language_code : str
            El código del idioma que el usuario desea establecer ("en" para inglés y "es" para español).
        
        Comportamiento:
        --------------
        - Verifica si el código del idioma es válido. Si no es "en" o "es", envía un mensaje informando las opciones disponibles.
        - Si el código del idioma es válido, guarda la preferencia de idioma del usuario en el diccionario compartido `user_language`.
        - Envía un mensaje de confirmación al usuario indicando que el idioma ha sido configurado correctamente.
        - Imprime mensajes de depuración para confirmar que la preferencia de idioma se ha actualizado correctamente.
        
        Ejemplo de uso:
        --------------
        El usuario escribe `!set_language es` en el chat de Discord, y el bot responde con:
        "Language set to es."
        """
        # Verificar si el código de idioma es válido
        if language_code not in ["en", "es"]:
            await ctx.send("Unsupported language. Available options: en, es")
            return

        # Guardar la preferencia de idioma del usuario en el diccionario compartido
        user_language[ctx.author.id] = language_code
        
        # Mensajes de depuración para confirmar la actualización
        print(f"User {ctx.author.id} set language to {language_code}")
        
        # Debugging statement to confirm language setting
        print(f"user_language dictionary after update: {user_language}")
        
        # Confirmar al usuario que el idioma ha sido configurado
        await ctx.send(f"Language set to {language_code}.")

# Función asíncrona de configuración para añadir el Cog al bot
async def setup(bot):
    """
    Añade el Cog SetLanguage al bot de manera asíncrona.
    
    Parámetros:
    ----------
    bot : commands.Bot
        La instancia del bot de Discord a la que se añadirá este Cog.
    
    Comportamiento:
    --------------
    - Verifica si el Cog `SetLanguage` ya está cargado en el bot.
    - Si no está cargado, lo añade al bot e imprime un mensaje de confirmación.
    - Si ya está cargado, imprime un mensaje indicando que se omitió la adición.
    
    Ejemplo de uso:
    --------------
    Esta función se llama normalmente al iniciar el bot para cargar la funcionalidad de este comando.
    """
    if not bot.get_cog("SetLanguage"):
        await bot.add_cog(SetLanguage(bot))
        print("SetLanguage Cog loaded successfully")
    else:
        print("SetLanguage Cog already loaded, skipping.")

# Declaración de depuración para verificar el diccionario user_language después de importar el módulo compartido
print(f"user_language dictionary after importing shared module: {user_language}")
