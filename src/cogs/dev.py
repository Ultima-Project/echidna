from discord import Embed
import discord
from discord.ext import commands
import re
import subprocess
import datetime


class Dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    ''' TODO: zio anime
    @commands.command(name='animepic')
    async def animepic(self, ctx, loop):
        while(loop):
            randomfile = random_file(ANIME_DIRECTORY)
            await ctx.send(file=File(randomfile))
    '''


    @commands.command(name='test')
    async def test(self, ctx, query):
        await ctx.send(query.strip().isnumeric())


    @commands.command(no_pm=False)
    @commands.is_owner()
    async def speedtest(self, ctx):
        try:
            channel = ctx.message.channel
            author = ctx.message.author
            user = author
            now = datetime.datetime.now()
            message12 = await ctx.send(':stopwatch: **Esecuzione dello speedtest. Questo potrebbe richiedere del tempo!** :stopwatch:')
            DOWNLOAD_RE = re.compile(r'Download: ([\d.]+) .bit')
            UPLOAD_RE = re.compile(r'Upload: ([\d.]+) .bit')
            PING_RE = re.compile(r'([\d.]+) ms')
            speedtest_result = await self.bot.loop.run_in_executor(None, speed_test)
            download = float(DOWNLOAD_RE.search(speedtest_result).group(1))
            upload = float(UPLOAD_RE.search(speedtest_result).group(1))
            ping = float(PING_RE.search(speedtest_result).group(1))
            message = 'I risultati del tuo speedtest sono:'
            message_down = '**{}** mbps'.format(download)
            message_up = '**{}** mbps'.format(upload)
            message_ping = '**{}** ms'.format(ping)
            embed = Embed(colour=0x47b81d, description=message)
            embed.title = 'Risultati speedtest'
            embed.add_field(name='Download', value=message_down)
            embed.add_field(name=' Upload', value=message_up)
            embed.add_field(name=' Ping', value=message_ping)
            embed.set_footer(text=now.strftime('%Y-%m-%d %H:%M'))
            await ctx.send(embed=embed)
        except KeyError:
            print('An error occured')


    @commands.command(name='spam')
    async def spam(self, ctx, message, loop):
        loop = int(loop)
        while loop:
            loop -= 1
            await ctx.send(message, delete_after=10.0)
        await ctx.message.delete()


    @commands.command()
    @commands.is_owner()
    async def clear(self, ctx, amount):
        await ctx.channel.purge(limit=int(amount)+1)


    @commands.command()
    @commands.bot_has_permissions(administrator=True)
    async def add_role(self, ctx):
        server = self.bot.get_guild()
        member = server.get_member()
        roles = server.roles
        print(roles)
        role = server.get_role()
        print(role)
        # print(role.permissions.administrator)
        print(self.bot.guilds)
        channel = server.get_channel()
        await channel.set_permissions(member, send_messages=True)
        # await member.add_roles(role)


    @commands.command()
    async def gerryscotti(self, ctx):
        await ctx.send('BUONASERA!')


    @commands.command()
    @commands.is_owner()
    async def region(self, ctx, *, region: str):
        regions = (
            'japan',
            'singapore',
            'eu-central',
            'europe',
            'india',
            'us-central',
            'london',
            'eu-west',
            'amsterdam',
            'brazil',
            'dubai',
            'us-west',
            'hongkong',
            'us-south',
            'southafrica',
            'us-east',
            'sydney',
            'frankfurt',
            'russia',
        )
        region = region.replace(' ', '-')
        if region not in regions:
            ctx.command.reset_cooldown(ctx)
            return await ctx.send(
                f'`{region}` non è stato trovato nell\'elenco delle regioni vocali Discord.'
            )
        try:
            await ctx.guild.edit(region=region)
        except discord.errors.Forbidden:
            return await ctx.send('Non ho i permessi per modificare le impostazioni di questa gilda.')
        except discord.errors.HTTPException:
            return await ctx.send(f'Errore: è stata trasmessa una regione del server non valida: `{region}`')
        await ctx.send(f'La regione del server vocale per `{ctx.guild.name}` è stato cambiato in `{region}`.')


def speed_test():
    return str(subprocess.check_output(['speedtest-cli'], stderr=subprocess.STDOUT))


def setup(bot):
    bot.add_cog(Dev(bot))
