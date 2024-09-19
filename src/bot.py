import discord
from discord.ext import commands
import yaml

# Load configuration from config.yaml
with open("config/config.yaml", 'r') as config_file:
    config = yaml.safe_load(config_file)

# Enable intents
intents = discord.Intents.default()
intents.messages = True  # Allow bot to read messages and respond to them
intents.message_content = True  # Enable message content intent

# Initialize the bot
bot = commands.Bot(command_prefix=config['bot']['prefix'], intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')  # Confirm bot login

# Async function to load extensions (command modules)
async def load_extensions():
    extensions = [
        'commands.log_expense',
        'commands.delete_expense',
        'commands.list_expenses',
        'commands.update_expense'
    ]

    for extension in extensions:
        try:
            await bot.load_extension(extension)
            print(f"Loaded extension {extension}")
        except Exception as e:
            print(f"Failed to load extension {extension}. Error: {e}")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await load_extensions()  # Load all command extensions

# Simple ping command to verify bot functionality
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")  # Basic command for testing bot responsiveness

# Run the bot
bot.run(config['bot']['token'])
