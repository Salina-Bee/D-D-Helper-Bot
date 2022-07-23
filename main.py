import os
import discord
from discord.ext import commands
import races
import misc

client = discord.Client()
bot = commands.Bot(command_prefix='!')
bot.add_cog(races.Races(bot))
bot.add_cog(misc.Misc(bot))
bot.run(os.getenv('TOKEN'))