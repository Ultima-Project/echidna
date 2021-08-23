import discord
from discord.ext import commands
from main import PREFIX


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f'OK ({self.bot.user})')
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game(PREFIX+'HELP | github.com/Ultima-Project/echidna'))


def setup(bot):
    bot.add_cog(Events(bot))
