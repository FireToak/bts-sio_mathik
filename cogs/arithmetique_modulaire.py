import discord
from discord.ext import commands

class Arithmetique_modulaire(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def nombre_premier(self, ctx, N: int):
        if N <= 1:
            return await ctx.send(f"❌ Le nombre `{N}` n'est pas premier.")
        for i in range(2, N):
            if N % i == 0:
                return await ctx.send(f"❌ Le nombre `{N}` n'est pas premier.")
        return await ctx.send(f"✅ Le nombre `{N}` est premier.")

async def setup(bot):
    await bot.add_cog(Arithmetique_modulaire(bot))