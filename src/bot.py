import discord
from discord.ext import commands
import yaml

# Load configuration from config.yaml
with open("config/config.yaml", 'r') as config_file:
    config = yaml.safe_load(config_file)

# Enable intents (adjust according to what your bot needs)
intents = discord.Intents.default()
intents.messages = True  # Allow the bot to listen to messages

# Initialize the bot with the necessary intents
bot = commands.Bot(command_prefix=config['bot']['prefix'], intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Load commands
extensions = ['commands.log_expense', 'commands.delete_expense']

for extension in extensions:
    try:
        bot.load_extension(extension)
        print(f"Loaded extension {extension}")
    except Exception as e:
        print(f"Failed to load extension {extension}. Error: {e}")

# Run the bot
bot.run(config['bot']['token'])
