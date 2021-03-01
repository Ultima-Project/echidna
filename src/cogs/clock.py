import datetime
import json
import pytz
import random
import urllib
import socket

import discord
import requests
from discord.ext import commands


class clock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="clock", pass_context=True, case_insensitive=True)
    async def clock(self, ctx):
        """Display hour in a country use the command -clock *country*"""

    @clock.command(name="montréal", aliases=["mtl", "montreal"], pass_context=True)
    async def clock_montreal(self, ctx):
        then = datetime.datetime.now(pytz.utc)
        utc = then.astimezone(pytz.timezone('America/Montreal'))
        time = utc.strftime("l'orario di Montreal in questo momento è: %H:%M:%S")
        await ctx.send(time)
        
    @clock.command(name="vancouver", pass_context=True)
    async def clock_vancouver(self, ctx):
        then = datetime.datetime.now(pytz.utc)
        utc = then.astimezone(pytz.timezone('America/Vancouver'))
        time = utc.strftime("l'orario di Vancouver in questo momento è: %H:%M:%S")
        await ctx.send(time)

    @clock.command(name="new-york",aliases=["ny", "n-y", "new york"], pass_context=True)
    async def clock_new_york(self, ctx):
        then = datetime.datetime.now(pytz.utc)
        utc = then.astimezone(pytz.timezone('America/New_York'))
        time = utc.strftime("l'orario di New York in questo momento è: %H:%M:%S")
        await ctx.send(time)
            
    @clock.command(name="la", aliases=["los-angeles", "losangeles", "l-a", "los angeles"], pass_context=True)
    async def clock_la(self, ctx):
        then = datetime.datetime.now(pytz.utc)
        utc = then.astimezone(pytz.timezone('America/Los_Angeles'))
        time = utc.strftime("l'orario di Los Angeles in questo momento è: %H:%M:%S")
        await ctx.send(time)
            
    @clock.command(name="paris", aliases=["baguette"],pass_context=True)
    async def clock_paris(self, ctx):
        then = datetime.datetime.now(pytz.utc)
        utc = then.astimezone(pytz.timezone('Europe/Paris'))
        time = utc.strftime("l'orario di Parigi in questo momento è: %H:%M:%S")
        await ctx.send(time)
    
    @clock.command(name="berlin", pass_context=True)
    async def clock_berlin(self, ctx):
        then = datetime.datetime.now(pytz.utc)
        utc = then.astimezone(pytz.timezone('Europe/Berlin'))
        time = utc.strftime("l'orario di Berlino in questo momento è: %H:%M:%S")
        await ctx.send(time)
    
    @clock.command(name="berne", aliases=["zurich", "bern"], pass_context=True)
    async def clock_berne(self, ctx):
        then = datetime.datetime.now(pytz.utc)
        utc = then.astimezone(pytz.timezone('Europe/Zurich'))
        time = utc.strftime("l'orario di Zurigo in questo momento è: %H:%M:%S")
        await ctx.send(time)
    
    @clock.command(name="tokyo", pass_context=True)
    async def clock_tokyo(self, ctx):
        then = datetime.datetime.now(pytz.utc)
        utc = then.astimezone(pytz.timezone('Asia/Tokyo'))
        time = utc.strftime("l'orario di Tokyo in questo momento è: %H:%M:%S")
        await ctx.send(time)

    @clock.command(name="moscou", aliases=["moscow", "moskova"], pass_context=True)
    async def clock_moscou(self, ctx):
        then = datetime.datetime.now(pytz.utc)
        utc = then.astimezone(pytz.timezone('Europe/Moscow'))
        time = utc.strftime("l'orario di Mosca in questo momento è: %H:%M:%S")
        await ctx.send(time)
    
    @clock.command(name="italia", pass_context=True)
    async def clock_italia(self, ctx):
        then = datetime.datetime.now(pytz.utc)
        utc = then.astimezone(pytz.timezone('Europe/Rome'))
        time = utc.strftime("l'orario di Italia in questo momento è: %H:%M:%S")
        await ctx.send(time)
        

def setup(bot):
    bot.add_cog(clock(bot))
