from discord.ext import commands
import os
import sys
import json

with open(os.path.join(sys.path[0], 'settings.json')) as settings:
    settings = json.load(settings)
    TOKEN = settings['token']
    PREFIX = settings['prefix']

bot = commands.Bot(command_prefix=PREFIX)


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded {extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded {extension}')


@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded {extension}')


for filename in os.listdir(os.path.join(sys.path[0], './cogs')):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

try:
    bot.run(TOKEN)
except:
    print('Invalid token or broken connection!')
