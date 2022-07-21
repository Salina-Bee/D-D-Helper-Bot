import os
import discord
from discord import activity
from discord.ext import commands

class Races(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self._last_member = None

  @commands.Cog.listener()
  async def on_ready(self):
    await self.bot.change_presence(activity=discord.Game("I'm online!"))

  @commands.command()
  async def races(self):
    
    