import asyncio
from discord import Embed, File
from discord.ext import commands
from random import choice
import nhentai
import rule34
from os_tools import random_file


class nsfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def ndoujin(self, ctx, *args):
        buttons = ['⏪', '◀', '⏹️', '▶', '⏩', '🔀', '🔒']

        query = ''
        for arg in args:
            query = query + arg + ' '
        query = query.strip()

        doujin, embed = ndoujin_embed(query)
        embed.set_footer(text='1 '+ctx.author.__str__())
        message = await ctx.send(embed=embed)

        for emoji in buttons:
            await message.add_reaction(emoji)

        private = True

        def check(reaction, user):
            if reaction.message.id == message.id and user == ctx.author or not private and reaction.message.id == message.id:
                return True
            return False

        page = 0
        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', check=check, timeout=60.0)
            except asyncio.TimeoutError:
                await ctx.message.delete()
                await message.delete()
                break
            else:
                if reaction.emoji == buttons[3] and page < len(doujin.pages)-1:
                    page += 1
                if reaction.emoji == buttons[1] and page > 0:
                    page -= 1
                if reaction.emoji == buttons[0]:
                    page = 0
                if reaction.emoji == buttons[4]:
                    page = len(doujin.pages)-1
                if reaction.emoji == buttons[2]:
                    await ctx.message.delete()
                    await message.delete()
                    break
                if reaction.emoji == buttons[5]:
                    doujin, embed = ndoujin_embed(query)
                    page = 0
                if reaction.emoji == buttons[6] or reaction.emoji == '🔓':
                    private = not private
                    message = await ctx.channel.fetch_message(message.id)
                    if message.reactions[6].emoji == buttons[6]:
                        await message.clear_reaction(buttons[6])
                        await message.add_reaction('🔓')
                    else:
                        await message.clear_reaction('🔓')
                        await message.add_reaction(buttons[6])
                await reaction.remove(user)
                embed.set_image(url=doujin.pages[page].url)
                embed.set_footer(text=str(page+1)+' '+ctx.author.__str__())
                await message.edit(embed=embed)


    @commands.command()
    async def r34(self, ctx, query: str):
        rule34_instance = rule34.Rule34(loop=asyncio.get_event_loop())
        images = await rule34_instance.getImages(query)
        await ctx.send(choice(images).file_url)


    @commands.command()
    async def animedir(self, ctx, number_of_images=1):
        for _ in range(number_of_images):
            await ctx.send(file=File(random_file('/home/wiichele/Immagini/Anime')))


def ndoujin_embed(query):
    doujin = search_ndoujin(query)
    tags = ntags(doujin)

    embed = Embed(title=doujin.titles['pretty'] +
                  ' https://nhentai.net/g/'+str(doujin.id), colour=0xb521a4)
    embed.set_image(url=doujin.cover)

    fields = [
        ('Parodies', tags['parody']),
        ('Character', tags['character']),
        ('Tags', tags['tag']),
        ('Artists', tags['artist']),
        ('Groups', tags['group']),
        ('Languages', tags['language']),
        ('Categories', tags['category']),
        ('Pages', len(doujin.pages)),
        ('Favorites', doujin.favorites)
    ]

    for name, value in fields:
        embed.add_field(name=name, value=value)

    return doujin, embed


def search_ndoujin(query: str):
    nid = 1
    if not query:
        nid = nhentai.get_random_id()
    elif query.isnumeric():
        nid = int(query)
    else:
        nid = choice(nhentai.search(query=query)).id
    return nhentai.get_doujin(id=nid)


def ntags(doujin):
    tags_names = {'parody': '', 'character': '', 'tag': '',
                  'artist': '', 'group': '', 'language': '', 'category': ''}

    for tag in doujin.tags:
        for key in tags_names:
            if tag.type == key:
                tags_names[key] += tag.name + ' '
                break

    for key in tags_names:
        if not len(tags_names[key]):
            tags_names[key] = 'None'

    return tags_names


def setup(bot):
    bot.add_cog(nsfw(bot))
