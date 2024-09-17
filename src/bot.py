import discord
from discord.ext import commands
import yaml

# Load configuration from config.yaml
with open("config/config.yaml", 'r') as config_file:
    config = yaml.safe_load(config_file)

# Enable intents (adjust according to what your bot needs)
intents = discord.Intents.default()
intents.message_content = True  # Allow the bot to read message content
intents.messages = True  # Allow the bot to listen to messages

# Initialize the bot with the necessary intents
bot = commands.Bot(command_prefix=config['bot']['prefix'], intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')  # Confirm bot login

# Async function to load extensions
async def load_extensions():
    extensions = ['commands.log_expense', 'commands.delete_expense']

    for extension in extensions:
        try:
            await bot.load_extension(extension)
            print(f"Loaded extension {extension}")
        except Exception as e:
            print(f"Failed to load extension {extension}. Error: {e}")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await load_extensions()  # Ensure extensions are loaded asynchronously

# Simple ping command to check if the bot is working
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Run the bot
bot.run(config['bot']['token'])
