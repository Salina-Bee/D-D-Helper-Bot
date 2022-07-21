import os
import discord
from discord.ext import commands
import races

client = discord.Client()
bot = commands.Bot(command_prefix='!')
bot.add_cog(races.Races(bot))
bot.run(os.getenv('TOKEN'))