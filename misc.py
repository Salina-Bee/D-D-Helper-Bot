import discord
from discord.ext import commands

class Misc(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def scream(self, ctx):
    await ctx.send('https://tenor.com/view/controlmypc-cat-screaming-discord-gif-20582295')
    
  @commands.command()
  async def bop(self, ctx):
    await ctx.send('https://tenor.com/bt7U4.gif')