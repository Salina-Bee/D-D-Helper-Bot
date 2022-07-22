import os
import discord
from discord.ext import commands
import races

client = discord.Client()
bot = commands.Bot(command_prefix='!')
bot.add_cog(races.Races(bot))

@bot.command()
async def scream(ctx):
  await ctx.send('https://tenor.com/view/controlmypc-cat-screaming-discord-gif-20582295')
bot.run(os.getenv('TOKEN'))