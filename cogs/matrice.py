import discord
from discord.ext import commands

class Addition_matrice(commands.Cogs):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def addition_matrice(self, ctx, A: list, B: list):
        # --- Vérification ---
        ligne_a = len(A)
        colone_a = len(A[0])
        ligne_b = len(B)
        colone_b = len(B[0])

        if ligne_a != ligne_a or colone_a != colone_b:
            print("Les deux matrices doivent avoir le même nombre de colones et de ligne.")
            continuer = False

        # Création de la liste C qui va stocker l'addition des deux matrices
        C = []

        

async def setup(bot):
    await bot.add_cog(Addition_matrice(bot))