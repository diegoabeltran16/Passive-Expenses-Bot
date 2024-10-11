# Import required modules from discord, yaml, and your own utilities
import discord
from discord.ext import commands
from src.commands.set_language import SetLanguage
from src.utils.lang import translate
from src.utils.shared import user_language

import yaml

# Load configuration from config.yaml
with open("src/config/config.yaml", 'r') as config_file:
    config = yaml.safe_load(config_file)

# Enable intents for handling messages and user interactions
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Initialize the bot with a command prefix and intents
bot = commands.Bot(command_prefix=config['bot']['prefix'], intents=intents)

# Function to load command extensions dynamically
async def load_extensions():
    """
    Asynchronously load command extensions (modules).
    """
    extensions = [
        'src.commands.log_expense',
        'src.commands.delete_expense',
        'src.commands.list_expenses',
        'src.commands.update_expense',
        'src.commands.set_language',
        'src.commands.log_report',     
        'src.commands.get_reports',    
        'src.commands.delete_report'   
    ]

    for extension in extensions:
        try:
            await bot.load_extension(extension)
            print(f"Loaded extension {extension}")
        except Exception as e:
            print(f"Failed to load extension {extension}. Error: {e}")

@bot.event
async def on_ready():
    """
    Event triggered when the bot successfully connects to Discord.
    """
    print(f'Logged in as {bot.user.name}')
    await load_extensions()

# Define a simple ping command to check if the bot is responsive
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Run the bot with the token from the configuration file
bot.run(config['bot']['token'])
