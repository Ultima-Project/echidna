from discord import Embed
from discord.ext import commands
from os import sys
from datetime import datetime
from os_tools import stats


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print('OK ({0})'.format(self.bot.user))


    @commands.command(name='stats')
    async def statistics(self, ctx):
        embed = Embed(title='Statistiche del bot', timestamp=datetime.utcnow())
        fields = stats()

        fields.append(
            ('Ping', str(round(self.bot.latency*1000, 1)) + ' ms', True))

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        await ctx.send(embed=embed)


    @commands.command(name='shutdown', hidden=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send('Mi sto spegnendo!')
        self.bot.logout()
        try:
            sys.exit()
        except SystemExit:
            pass


    @commands.command(pass_context=True)
    async def revimg(self, ctx, url=None):
        if url is not None:
            await ctx.message.delete()
        if url is None:
            try:
                url = ctx.message.attachments[0].url
            except IndexError:
                return await ctx.send('No URL or Image detected. Please try again!')
        embed = Embed(title='Reverse Image Details', color=16776960)
        embed.add_field(
            name='SauceNao', value=f'[SauceNao Image Results](https://saucenao.com/search.php?url={url})', inline=True)
        embed.add_field(
            name='Google', value=f'[Google Image Results](https://www.google.com/searchbyimage?&image_url={url})', inline=True)
        embed.add_field(
            name='TinEye', value=f'[Tineye Image Results](https://www.tineye.com/search?url={url})', inline=True)
        embed.add_field(
            name='IQBD', value=f'[IQBD Image Results](https://iqdb.org/?url={url})', inline=True)
        embed.add_field(
            name='Yandex', value=f'[Yandex Image Results](https://yandex.com/images/search?url={url}&rpt=imageview)', inline=True)
        embed.set_thumbnail(url=url)
        await ctx.send(embed=embed)


    @commands.command(name='github', pass_context=True)
    async def _git(self, ctx):
        text = 'Vuoi vedere il nostro codice sorgente?' \
               'o vuoi aiutarci ad implementare nuove funzioni? ' \
               'ecco a te il nostro link di github :sunglasses: \n https://github.com/Ultima-Project/echidna'
        em = Embed(title='Github Repo Echidna',
                   description=text, colour=0xE9D460)
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Utility(bot))
