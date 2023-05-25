import discord
import json
import asyncio
from discord.ext import commands
from discord.ext import tasks
class Meta(commands.Cog):
  def __init__(self, client):
   self.client = client
        
  @commands.Cog.listener()
  async def on_ready(self):
      print('setup is ready lol')
 

  
  #change prefix command
  @commands.command(name='Change Prefix', aliases=['changeprefix'])
  @commands.has_permissions(administrator=True)
  async def prefix(self, ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send('**Prefix changed successfully to:"{prefix}"')

def setup(client):
    client.add_cog(Meta(client))
