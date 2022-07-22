import os
import discord
import requests
import json
from discord import activity
from discord.ext import commands

class Races(commands.Cog):

  racesList = list()
  
  def __init__(self, bot):
    self.bot = bot
    self.racesList = self.get_default_races()

  #get default races
  def get_default_races(self):
    response = requests.get("https://api.open5e.com/races/?format=json")
    json_data = json.loads(response.text)
    races = json_data['results']
    rlist = list()
    for i in races:
      rlist.append(i['name'])
    return rlist

  #bot is ready
  @commands.Cog.listener()
  async def on_ready(self):
    await self.bot.change_presence(activity=discord.Game("I'm online!"))
    print('Ready!')

  #returns the list of races (default and new ones)
  @commands.command()
  async def races(self, ctx):
    str = ""
    for i in self.racesList:
      str += "\n" + i
    await ctx.send('__List of Races:__ (use !race <race> for detailed info)' + str)

  #returns information regarding given race
  @commands.command()
  async def race(self, ctx, *, arg):
    await ctx.send(arg)

  #error handling of race()
  @race.error
  async def race_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send('Missing the name of the race. Command usage: !race <race>')
      
  #adds a race to racesList 
  @commands.command()
  async def add_race(self, ctx, *, arg):
    await ctx.send('Add race?')
    id = ctx.guild.id #get server id
    name = ctx.guild.name

  #error handling of add_race()
  @add_race.error
  async def add_race_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send('Missing the name of the race to be added. Command usage: !add_race <race>')
  
  #removes a race from racesList
  @commands.command()
  async def del_race(self, ctx, *, arg):
    if (arg in self.get_default_races()):
      await ctx.send('Cannot delete a default race.')
    else:
      await ctx.send('Removed race.')

  #error handling of del_race()
  @del_race.error
  async def del_race_error(self, ctx, error):
    if isistance(error, commands.MissingRequiredArgument):
      await ctx.send('Missing the name of the race to be deleted. Command usage: !del_race <race>')