import discord
import os
from discord.ext import commands

# Récupération du token du bot discord
TOKEN_BOT_DISCORD = os.getenv('TOKEN_BOT_DISCORD')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print(f"Logged on as {bot.user}.")

@bot.event
async def setup_hook():
    await load_cogs()

bot.run(TOKEN_BOT_DISCORD)