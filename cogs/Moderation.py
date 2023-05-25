import time
import discord
import json
import asyncio
from discord.ext import commands
from discord.ext import tasks

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.Cog.listener()
    async def on_ready(self):
      print('moderation is ready lol')


       #ban command
    @commands.command(name='Ban')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
      await member.ban(reason=reason)
      await ctx.send(f'**Banned. L**')
      
      
      
      
      
      
      #kick command
    @commands.command(name='Kick')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
      await member.kick(reason=reason)
      await ctx.send(f'**Kicked. L**')
      
      
      
      
      
      #unban command
    @commands.command(name='Unban')
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
     banned_users = await ctx.guild.bans()
     member_name, member_discriminator = member.split('#')
  
  
     for ban_entry in banned_users:
      user = ban_entry.user
      
      if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f'**Unbanned. dont get banned again lol **')
        return


      
    @commands.command(name='Purge')
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=5):
        channel = ctx.message.channel
        await ctx.message.delete()
        await channel.purge(limit=amount)

def setup(client):
    client.add_cog(Moderation(client))
