import asyncio
from discord.ext import commands
from discord.utils import get
from os import path


class management(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ruoli")
    async def ruoli(self, ctx):
        print(ctx.guild.roles)

    @commands.command(name="setdefaultrole")
    async def set_default_role(self, ctx, default):
        buttons = ['❌', '✅']

        server_id = ctx.guild.id
        role = get(ctx.guild.roles, name=default)
        if role is None:
            await ctx.send("Ruolo non trovato!")
            return

        file_r = open(path.join(path.expanduser("~") +
                                "/Vittroia.py/default_rules.vtt"), "r")

        credentials = file_r.readlines()
        count = 0
        for line in credentials:
            if line.startswith(str(server_id)):
                role_id = line.strip()[line.strip().index(" "):]
                if int(role_id) != role.id:
                    message = await ctx.send("Ruolo di default già impostato, modificare?", delete_after=90.0)
                    for emoji in buttons:
                        await message.add_reaction(emoji)

                    def check(reaction, user, message=message):
                        return reaction.message.id == message.id and user == ctx.author

                    while True:
                        try:
                            reaction, user = await self.bot.wait_for('reaction_add', check=check, timeout=60.0)
                        except asyncio.TimeoutError:
                            await ctx.message.delete()
                            await message.delete()
                            break
                        else:
                            if reaction.emoji == buttons[0]:
                                await ctx.send("Ruolo di default non modificato", delete_after=90.0)
                                return
                            if reaction.emoji == buttons[1]:
                                credentials[count] = str(
                                    server_id) + " " + str(role.id) + "\n"
                                file_w = open(path.join(path.expanduser(
                                    "~") + "/Vittroia.py/default_rules.vtt"), 'w')
                                file_w.writelines(credentials)
                                await ctx.send("Ruolo di default aggiornato", delete_after=90.0)
                                return
                else:
                    await ctx.send("Ruolo di default gia impostato", delete_after=90.0)
                    return
            count += 1
        credentials.append(str(server_id) + " " + str(role.id) + "\n")
        file_w = open(path.join(path.expanduser("~") +
                                "/Vittroia.py/default_rules.vtt"), 'w')
        file_w.writelines(credentials)
        await ctx.send("Ruolo di default impostato", delete_after=90.0)
        return

    @commands.Cog.listener()
    async def on_member_join(self, member):
        server_id = member.guild.id

        file_r = open(path.join(path.expanduser("~") +
                                "/Vittroia.py/default_rules.vtt"), 'r')
        credentials = file_r.readlines()
        for line in credentials:
            if line.startswith(str(server_id)):
                role_id = line.strip()[line.strip().index(" "):]
                await member.add_roles(member.guild.get_role(int(role_id)))
                return


def setup(bot):
    bot.add_cog(management(bot))
