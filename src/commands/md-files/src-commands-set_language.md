# set_language

## Descripción General
El objetivo principal de este código es permitir a los usuarios establecer su idioma preferido para las respuestas del bot en Discord. El código define un "Cog" llamado SetLanguage que gestiona el comando set_language, lo que permite a los usuarios seleccionar entre inglés ("en") y español ("es"). Este ajuste se guarda en un diccionario compartido, user_language, para ser utilizado por otras partes del bot.

## Pseudo Codigo

## Codigo

```
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


```

## PseudoCodigo

```
INICIO

IMPORTAR los módulos necesarios:
    - commands de discord.ext para manejar comandos de Discord
    - user_language de utils.shared para acceder y actualizar las preferencias de idioma de los usuarios

DEFINIR la clase SetLanguage como un "Cog" para manejar el comando de configuración de idioma
    MÉTODO __init__(self, bot):
        GUARDAR la instancia del bot en un atributo de la clase

    DEFINIR el método set_language como un comando
        RECIBIR los parámetros: ctx (contexto del comando) y language_code (código del idioma deseado)

        VERIFICAR si language_code es un idioma válido ("en" o "es")
            SI NO es válido:
                ENVIAR un mensaje al usuario indicando que las opciones disponibles son "en" y "es"
                TERMINAR la ejecución del comando

        ACTUALIZAR el diccionario user_language con la preferencia de idioma del usuario
            ASIGNAR language_code a la clave correspondiente al ID del usuario (ctx.author.id)

        IMPRIMIR un mensaje de depuración confirmando que el idioma del usuario ha sido configurado correctamente
        IMPRIMIR el contenido actual del diccionario user_language para verificar que la actualización fue correcta

        ENVIAR un mensaje de confirmación al usuario indicando que el idioma ha sido configurado

DEFINIR la función asíncrona setup(bot):
    VERIFICAR si el bot ya tiene cargado el Cog "SetLanguage"
        SI NO está cargado:
            AÑADIR el Cog SetLanguage al bot y mostrar un mensaje de confirmación
        SI ya está cargado:
            MOSTRAR un mensaje indicando que la carga fue omitida

IMPRIMIR el contenido actual del diccionario user_language para confirmar que está importado correctamente

FIN

```