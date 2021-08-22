from datetime import datetime
import pytz
from discord.ext import commands


class clock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.group(name='clock', pass_context=True, case_insensitive=True, brief='Display hour in a country use the command -clock *country*')
    async def clock(self, ctx):
        pass


    @clock.command(name='montréal', aliases=['mtl', 'montreal'], pass_context=True)
    async def clock_montreal(self, ctx):
        city = 'Montreal'
        timezone = 'America/Montreal'
        await ctx.send(datetime_with_timezone(city, timezone))


    @clock.command(name='vancouver', pass_context=True)
    async def clock_vancouver(self, ctx):
        city = 'Vancouver'
        timezone = 'America/Vancouver'
        await ctx.send(datetime_with_timezone(city, timezone))


    @clock.command(name='new-york', aliases=['ny', 'n-y', 'new york'], pass_context=True)
    async def clock_new_york(self, ctx):
        city = 'New York'
        timezone = 'America/New_York'
        await ctx.send(datetime_with_timezone(city, timezone))


    @clock.command(name='la', aliases=['los-angeles', 'losangeles', 'l-a', 'los angeles'], pass_context=True)
    async def clock_la(self, ctx):
        city = 'Los Angeles'
        timezone = 'America/Los_Angeles'
        await ctx.send(datetime_with_timezone(city, timezone))


    @clock.command(name='paris', aliases=['baguette'], pass_context=True)
    async def clock_paris(self, ctx):
        city = 'Parigi'
        timezone = 'Europe/Paris'
        await ctx.send(datetime_with_timezone(city, timezone))


    @clock.command(name='berlin', pass_context=True)
    async def clock_berlin(self, ctx):
        city = 'Berlino'
        timezone = 'Europe/Berlin'
        await ctx.send(datetime_with_timezone(city, timezone))


    @clock.command(name='berne', aliases=['zurich', 'bern'], pass_context=True)
    async def clock_berne(self, ctx):
        city = 'Zurigo'
        timezone = 'Europe/Zurich'
        await ctx.send(datetime_with_timezone(city, timezone))


    @clock.command(name='tokyo', pass_context=True)
    async def clock_tokyo(self, ctx):
        city = 'Tokyo'
        timezone = 'Asia/Tokyo'
        await ctx.send(datetime_with_timezone(city, timezone))


    @clock.command(name='moscou', aliases=['moscow', 'moskova'], pass_context=True)
    async def clock_moscou(self, ctx):
        city = 'Mosca'
        timezone = 'Europe/Moscow'
        await ctx.send(datetime_with_timezone(city, timezone))


    @clock.command(name='italia', pass_context=True)
    async def clock_italia(self, ctx):
        city = 'Italia'
        timezone = 'Europe/Rome'
        await ctx.send(datetime_with_timezone(city, timezone))


def datetime_with_timezone(city: str, timezone: str):
    now = datetime.now(pytz.utc)
    utc = now.astimezone(pytz.timezone(timezone))
    str = 'L\'orario di {0} in questo momento è %H:%M:%S'
    time = utc.strftime(str.format(city))
    return time


def setup(bot):
    bot.add_cog(clock(bot))
