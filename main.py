
#import packages
import discord
import json
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
from discord.ext import *
from discord.utils import find

client = discord.Client()


#allows for a changeable prefix
def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]


#makes commands case-insensitive
client = commands.Bot(command_prefix= (get_prefix), case_insensitive=(True))
#client = commands.Bot(command_prefix = get_prefix)


#prints a message in console when the bot is sucessfully logged in

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('the cello.'))
    print("bot is on lol")
    


#prefixes 2: electric boogaloo

def get_prefix(client, message):
 with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix)

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    

  

#cogs stuff

@client.command(hidden=True)
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')
  
@client.command(hidden=True)
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('TOKEN'))
