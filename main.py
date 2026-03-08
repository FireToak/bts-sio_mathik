import discord
import os
from discord.ext import commands

# Récupération du token du bot discord
TOKEN_BOT_DISCORD = os.getenv('TOKEN_BOT_DISCORD')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f"Logged on as {bot.user}.")

@bot.command()
async def est_premier(ctx, N: int):
    if N <= 1:
        return await ctx.send("Le nombre n'est pas premier.")
    for i in range(2, N):
        reste = N % i
        if reste == 0:
            return await ctx.send("Le nombre n'est pas premier.")
    return await ctx.send("Le nombre est premier.")

bot.run(TOKEN_BOT_DISCORD)