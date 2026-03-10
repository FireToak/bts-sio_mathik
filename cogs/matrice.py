import discord
from discord.ext import commands

class Addition_matrice(commands.Cogs):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Addition_matrice(bot))