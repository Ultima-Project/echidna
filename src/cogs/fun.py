from datetime import datetime, date
from discord import Embed, Member, Colour, HTTPException
from discord.ext import commands
from random import choice, randint
from urllib.request import urlopen
import json
import requests


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def dado(self, ctx):
        await ctx.trigger_typing()
        await ctx.send((choice(['Uno', 'Due', 'Tre', 'Quattro', 'Cinque', 'Sei'])))


    @commands.command()
    async def rmeme(self, ctx):
        with urlopen('https://meme-api.herokuapp.com/gimme') as url:
            data = json.loads(url.read().decode())
            title = data['title']
            url = data['url']
            sub_reddit = data['subreddit']

        embed = Embed(
            title=title,
            description='from: ' + sub_reddit + ' subreddit',
            colour=0x009BFF
        )
        embed.set_image(url=url)
        await ctx.send(embed=embed)


    @commands.command()
    async def duel(self, ctx, *, user: Member):
        random = randint(2, 120)
        if user.id == ctx.bot.user.id:
            await ctx.send('Non sono il tipo da combattimento')
        else:
            await ctx.send(f'{ctx.author.mention} e {user.mention} hanno duellato per {random} ore! \
                           \nÈ stata una lunga battaglia accesa, ma {choice([ctx.author.mention, user.mention])} è uscito vittorioso!')


    @commands.command(name='commands')
    async def list_commands(self, ctx):
        await ctx.send('Non dirmi cosa fare.')


    @commands.command()
    async def natale(self, ctx):

        now = datetime.datetime.now()
        today = date(now.year, now.month, now.day)

        year = now.year
        if (now.month == 12 and now.day > 25):
            year = now.year + 1

        xmasday = date(year, 12, 25)

        delta = xmasday - today

        await ctx.send(':date: **' + str(delta.days) + '** giorni rimasti fino a Natale! :christmas_tree:')


    @commands.command(name='corona')
    async def country(self, ctx, country_string: str):
        r = requests.get('https://coronavirus-19-api.herokuapp.com/countries')
        json = r.json()

        for index, country in enumerate(json):
            if country['country'].lower() == country_string.lower():
                embed = Embed(title='Statistiche COVID-19 per '+country['country']+' - rango '+str(
                    index+1), description=f'', color=Colour.red())
                embed.add_field(name='Casi totali',
                                value=country['cases'], inline=False)
                embed.add_field(name='Morti totali',
                                value=country['deaths'], inline=False)
                embed.add_field(name='Recuperi totali',
                                value=country['recovered'], inline=False)
                embed.add_field(name='I nuovi casi di oggi',
                                value=country['todayCases'], inline=False)
                embed.add_field(name='Le nuove morti di oggi',
                                value=country['todayDeaths'], inline=False)
                embed.add_field(name='Casi positivi',
                                value=country['active'], inline=False)
                embed.add_field(name='Casi attivi in ​​condizioni critiche',
                                value=country['critical'], inline=False)
                embed.add_field(name='Casi per milione di cittadini',
                                value=country['casesPerOneMillion'], inline=False)
                embed.set_footer(
                    text='Queste informazioni non sono al 100'+'%'+' accurate')
                await ctx.send(embed=embed)
                return

        await ctx.send('Non sono riuscito a trovare quel paese. Scrivilo in inglese')


    async def send_leaderboard(self, ctx):
        r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
        json = r.json()
        total_cases = json['cases']
        total_deaths = json['deaths']
        total_recovered = json['recovered']

        r = requests.get('https://coronavirus-19-api.herokuapp.com/countries')
        json = r.json()

        countries = json[:10]

        embed = Embed(title='Statistiche COVID-19',
                      description=f'{total_cases}/{total_deaths}/{total_recovered} **(Casi/Morti/Recuperati)**', color=Colour.red())

        for i in range(len(countries)):
            country = countries[i]
            embed.add_field(name=str(
                i+1)+'. '+country['country'], value=f'{country["cases"]}/{country["deaths"]}/{country["recovered"]} (C/D/R) **+{country["todayCases"]}/{country["todayDeaths"]} (C/D)**', inline=False)

        channel = self.bot.get_channel(self.channel_id)
        embed.set_footer(
            text='Queste informazioni non sono al 100'+'%'+' accurate')

        await ctx.send(embed=embed)


    @commands.command(pass_context=True, no_pm=True)
    async def avatar(self, ctx, user: Member):
        try:
            colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            embed = Embed(colour=Colour(value=colour))
            embed.set_author(name='{}\'s avatar:'.format(
                user.name), url=user.avatar_url)
            embed.set_image(url=user.avatar_url)

            await ctx.send(embed=embed)
        except HTTPException:
            await ctx.send(user.avatar_url)
            print('Mancano i permessi per l\'embed')


    @commands.command()
    async def culo(self, ctx):
        await ctx.send('ლ(́◉◞౪◟◉‵ლ)')


    @commands.command()
    async def squat(self, ctx):
        random = randint(2, 1000)
        random1 = randint(4, 90)
        await ctx.send(f'{ctx.author.mention} mette sulla faccia del gioco e fa {random} squat in {random1} minuti. Ne vale la pena!')


def setup(bot):
    bot.add_cog(Fun(bot))
