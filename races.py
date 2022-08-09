import discord
import requests
import json
from discord.ext import commands

class Races(commands.Cog):

  racesList = list()
  importantInfo = ['desc', 'asi_desc', 'age', 'alignment', 'size', 'speed_desc', 'languages', 'vision', 'traits']

  def __init__(self, bot):
    self.bot = bot
    self.racesList = self.get_default_races()

  #bot is ready
  @commands.Cog.listener()
  async def on_ready(self):
    await self.bot.change_presence(activity=discord.Game("I'm online!"))
    print('Ready!')

  #get default races
  def get_default_races(self):
    response = requests.get("https://api.open5e.com/races/?format=json")
    json_data = json.loads(response.text)
    races = json_data['results']
    rlist = list()
    for i in races:
      rlist.append(i['name'])
    return rlist
  
  #returns the list of races (default and new ones)
  @commands.command()
  async def races(self, ctx):
    str = ""
    for i in self.racesList:
      str += "\n" + i
    await ctx.send('__List of Races:__ (use !race <race> for detailed info)' + str)

  #get default race info
  def get_default_race_info(self, ctx, race):

    # get json and search for race
    response = requests.get("https://api.open5e.com/races/?format=json")
    json_data = json.loads(response.text)
    raceInfo = json_data['results'] 
    res = next((sub for sub in raceInfo if sub['slug'] == race.lower()), None) 
    print(res)

    # print necessary info
    embed = discord.Embed(
      title = res['name'],
        color=discord.Color.blue())
    num = res['desc'].find("Traits") + 6
    embed.add_field(name="Description", value=res['desc'][num:], inline=False)
    embed.add_field(name="Ability Score Increase", value=res['asi_desc'][29:], inline=False)
    embed.add_field(name="Age", value=res['age'][10:], inline=False)
    embed.add_field(name="Alignment", value=res['alignment'][16:], inline=False)
    embed.add_field(name="Size", value=res['size'][11:], inline=False)
    embed.add_field(name="Speed", value=res['speed_desc'][12:], inline=False)
    embed.add_field(name="Languages", value=res['languages'][16:], inline=False)
    embed.add_field(name="Vision", value=res['vision'], inline=False)
    embed.add_field(name="Traits", value=res['traits'], inline=False)
    return embed
      
  #returns information regarding given race
  @commands.command()
  async def race(self, ctx, *, arg):
    tempRacesList = [x.lower() for x in self.racesList]
    if (arg.lower() not in tempRacesList):
      await ctx.send('No such race found. Please check !races to ensure that you spelt it correctly and that it exists in the database.')
    else:
      embed = self.get_default_race_info(ctx, arg)
      await ctx.send(embed=embed)

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
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send('Missing the name of the race to be deleted. Command usage: !del_race <race>')