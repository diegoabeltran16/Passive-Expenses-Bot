# src/bot.py

## General Description
The main goal of this script is to set up a Discord bot that can interact with users, respond to commands, and dynamically load various command extensions. This bot provides features such as logging expenses, deleting expenses, listing expenses, updating expenses, and setting user language preferences. The bot also includes a basic "ping" command to verify its responsiveness.


## Pseudocode
```
1. **Import necessary modules**
   - Import required packages from Discord and YAML.
   - Import custom command modules for extended functionality.

2. **Load configuration from config.yaml**
   - Open and load the configuration file (`config.yaml`) to retrieve necessary settings.

3. **Enable Discord Intents**
   - Create intents that allow the bot to manage events like reading and responding to messages.

4. **Initialize the Bot**
   - Create a bot instance (`commands.Bot`) with the desired prefix and enabled intents.

5. **Define asynchronous function to load extensions**
   - Define an `async` function to load extensions (modules of commands).
   - Create a list of extensions to be loaded, including `log_expense`, `delete_expense`, `list_expenses`, `update_expense`, and `set_language`.
   - Use a loop to load each extension and print a success or failure message for each one.

6. **Define the "on_ready" event**
   - Create an `async` function (`on_ready`) that triggers when the bot successfully connects to Discord.
   - Print the bot's name to confirm successful login.
   - Call `load_extensions()` to load all command extensions after the bot is ready.

7. **Define the "ping" command**
   - Define a simple command named "ping" to verify the bot's response.
   - Reply with "Pong!" when the command is invoked.

8. **Run the bot**
   - Use the bot token from the configuration file to run the bot (`bot.run(config['bot']['token'])`).

```

## Code

```
# Importa los módulos necesarios de los paquetes discord y yaml.
import discord
from discord.ext import commands
from src.commands.set_language import SetLanguage  # Asegura que el path sea correcto para el Cog
from src.utils.lang import translate  # Importa la función de traducción
from src.utils.shared import user_language  # Importa el diccionario compartido de preferencias de idioma

import yaml

# Cargar la configuración desde el archivo config.yaml
with open("src/config/config.yaml", 'r') as config_file:
    config = yaml.safe_load(config_file)

# Habilita intents para permitir que el bot gestione eventos como mensajes e interacciones con los usuarios.
intents = discord.Intents.default()
intents.messages = True  # Permitir que el bot lea y responda a los mensajes.
intents.message_content = True  # Habilita la intención de contenido de mensaje para acceder al contenido de texto de los mensajes.

# Inicializa la instancia del bot con el prefijo y los intents cargados desde el archivo de configuración.
bot = commands.Bot(command_prefix=config['bot']['prefix'], intents=intents)

# Función asíncrona para cargar extensiones de comandos dinámicamente.
async def load_extensions():
    """
    Carga asíncrona de extensiones (módulos de comandos).
    """
    extensions = [
        'src.commands.log_expense',
        'src.commands.delete_expense',
        'src.commands.list_expenses',
        'src.commands.update_expense',
        'src.commands.set_language'  # Asegura el path correcto para set_language
    ]

    for extension in extensions:
        try:
            # Intente cargar cada extensión de comando.
            await bot.load_extension(extension)
            print(f"Loaded extension {extension}")
        except Exception as e:
            # Si la carga falla, imprima el error.
            print(f"Failed to load extension {extension}. Error: {e}")

@bot.event
async def on_ready():
    """
    Evento que se activa cuando el bot se conecta con éxito a Discord.
    """
    print(f'Logged in as {bot.user.name}')
    await load_extensions()  # Carga todas las extensiones de comandos después de que el bot esté listo.

# Define un simple comando ping para probar si el bot responde.
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")  # Responde con "¡Pong!" para verificar la capacidad de respuesta del bot.

# Ejecuta el bot con el token proporcionado en el archivo de configuración.
bot.run(config['bot']['token'])

```
## Testing 
tests/test_bot.py

**Main Goal:**
The main goal of this code is to test the basic functionality of the bot, including command handling and dynamic extension loading, without actually running the bot or interacting with Discord servers. It aims to validate that the bot can correctly respond to a known command (“!ping”), load its extensions properly, and handle scenarios where a command is not recognized.

### Testing Pseudocode
```
1. **Import necessary modules**
    - Import required modules for testing, discord, and mocking functionalities.

2. **Add path for importing bot**
    - Adjust the system path to allow importing from the "src" directory.

3. **Import classes and methods from bot**
    - Import the bot instance and the `load_extensions` function from the bot module.

4. **Define `TestBot` class inheriting from `unittest.IsolatedAsyncioTestCase`**

5. **Define `asyncSetUp` method**
    - Create a bot instance with a command prefix "!" and default intents.
    - Patch the bot's `run` method to prevent it from actually running during tests.
    - Mock the bot user object to simulate a logged-in bot.
    - Mock the `ctx` (context) object to simulate a command invocation context.

6. **Define `asyncTearDown` method**
    - Stop the `run` patcher after each test.

7. **Define `test_ping_command` method**
    - Add a `ping` command to the bot which responds with "Pong!".
    - Retrieve the command object for "ping".
    - Invoke the `ping` command with the mocked context (`ctx`).
    - Assert that the bot sends the message "Pong!".

8. **Define `test_load_extensions` method**
    - Patch the `load_extension` method of the bot to avoid actually loading the extensions.
    - Call `load_extensions()` to load the command extensions.
    - Assert that each extension is loaded correctly by checking calls to `load_extension`.

9. **Define `test_command_invocation` method**
    - Simulate a command (`!nonexistent_command`) that does not exist.
    - Create a context (`ctx`) for the nonexistent command.
    - Invoke the command using the bot.
    - Assert that no response was sent (`ctx.send` should not be called).

10. **Run tests**
    - Call `unittest.main()` to run the defined test cases.

```

### Testing code
```
import unittest
import sys
import os
import discord
from unittest.mock import AsyncMock, MagicMock, patch
from discord.ext import commands

# Add the correct path for imports to include the src directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from bot import bot, load_extensions

class TestBot(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        """
        Set up the bot instance before each test.
        """
        intents = discord.Intents.default()
        self.bot = commands.Bot(command_prefix="!", intents=intents)

        # Patch the run method to prevent the bot from actually running during tests
        self.run_patcher = patch.object(self.bot, 'run', return_value=None)
        self.mock_run = self.run_patcher.start()

        # Mock the bot's user object to simulate the bot being logged in
        self.bot.user = MagicMock()
        self.bot.user.id = 12345  # Set a mock bot user ID

        # Mock the send method for ctx
        self.ctx = MagicMock()
        self.ctx.send = AsyncMock()
        self.ctx.author.id = 1
        self.ctx.message = MagicMock()
        self.ctx.message.content = "!ping"
        self.ctx.message.author = self.ctx.author

    async def asyncTearDown(self):
        """
        Clean up after each test.
        """
        self.run_patcher.stop()

    async def test_ping_command(self):
        """
        Test the ping command.
        """
        @self.bot.command(name='ping')
        async def ping(ctx):
            await ctx.send("Pong!")

        # Get the command object and invoke it directly
        command = self.bot.get_command('ping')
        await command(self.ctx)
        
        # Assert that the bot sends the "Pong!" message
        self.ctx.send.assert_called_with("Pong!")

    async def test_load_extensions(self):
        """
        Test loading extensions dynamically.
        """
        # Patch the bot's load_extension method
        with patch.object(self.bot, 'load_extension', new_callable=AsyncMock) as mock_load_extension:
            # Override bot instance in load_extensions function for testing
            await load_extensions()  # Call the method to load extensions

            # Check that extensions were attempted to be loaded
            extensions = [
                'src.commands.log_expense',
                'src.commands.delete_expense',
                'src.commands.list_expenses',
                'src.commands.update_expense',
                'src.commands.set_language'
            ]
            for ext in extensions:
                mock_load_extension.assert_any_call(ext)

    async def test_command_invocation(self):
        """
        Test invoking a non-existent command to ensure proper handling.
        """
        # Create a fake message object for a non-existent command
        self.ctx.message.content = "!nonexistent_command"
        message = self.ctx.message
        ctx = await self.bot.get_context(message)

        # Invoke the non-existent command
        await self.bot.invoke(ctx)

        # Verify that the bot doesn't call ctx.send() because the command doesn't exist
        self.ctx.send.assert_not_called()

if __name__ == '__main__':
    unittest.main()
```