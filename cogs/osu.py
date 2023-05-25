import osutools
import requests
import os
import time
import discord
import json
import asyncio
from discord.ext import commands
from discord.ext import tasks

class osu!(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        
    @commands.command(name='osu!')
    async def osu(self, ctx, username="peppy"):
      me = osu.fetch_user(username=username)
      await ctx.message.delete()
      await ctx.send(f"**{me} | {me.pp}pp | #{me.rank} Global**")
    
    @commands.command(name='beatmap')
    async def beatmap(self, ctx, beatmapID=0):
      beatmap = osu.fetch_map(map_id=beatmapID)
      await ctx.send(f"{beatmap.song_title} [{beatmap.difficulty_name}] | {beatmap.artist} | {beatmap.creator_name}")
    
    
def setup(client):
    client.add_cog(osu!(client))
