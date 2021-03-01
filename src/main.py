from discord.ext import commands
from os import listdir
from time import sleep
from json import load

with open("settings.json", 'r') as settings:
    settings = load(settings)
    TOKEN = settings['token']
    PREFIX = settings['prefix']
bot = commands.Bot(command_prefix=PREFIX)


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f"Loaded {extension}")


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f"Unloaded {extension}")


@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f"Reloaded {extension}")

for filename in listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f'cogs.{filename[:-3]}')

try:
    bot.run(TOKEN)
except:
    print("Invalid token or broken connection!")
    sleep(3)
