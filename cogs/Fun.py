#imports some packages
import variables
import datetime
import random
import asyncio
import time
import discord
from discord.ext import commands
#shows the class/catergory when you do .help


class Fun(commands.Cog):
  
  def __init__(self, client):
    self.client = client
    
    #prints into the console once ready
    
  @commands.Cog.listener()
  async def on_ready(self):
    print('fun is ready lol')
    
  #commands
    
  @commands.command(name='Ping')
  async def ping(self, ctx):
    await ctx.message.delete()
    time_1 = time.perf_counter()
    await ctx.trigger_typing()
    time_2 = time.perf_counter()
    ping = round((time_2-time_1)*1000)
    await ctx.send(f"**Pong! {ping}ms**")
    #await ctx.send('Pong! {0}'.format(round(client.latency, 1)))
   
  @commands.command(name='Rate',aliases=['r8'])
  async def rate(self, ctx):
    await ctx.message.delete()
    await ctx.send(f"{ctx.message.author.mention} {random.choice(variables.RATINGS)}")

    
  @commands.command(name='8 Ball', aliases=['eightball','8ball','8b'])
  async def eightball(self, ctx, question=str):
    await ctx.message.delete()
    await ctx.send(ctx.message.author.mention + " " + random.choice(variables.BALLANSWERS))
   
  @commands.command(name='Fun Fact', aliases=['funfact','fact','ff'])
  async def funfact(self, ctx):
    await ctx.message.delete()
    await ctx.send("Fun Fact: "+ random.choice(variables.FACTS)) 
  '''    
  @commands.command()
  async def testembed(self, ctx):
    embed = discord.Embed(title="A", description="B")
    embed.add_field(name="C", value="D")
    await ctx.send(embed=embed)
  '''
def setup(client):
  client.add_cog(Fun(client))
