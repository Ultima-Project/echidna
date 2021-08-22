import asyncio
from discord.ext import commands
from discord.utils import get
from os import path
import discord


class management(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, context, member: discord.Member, *, reason="Not specified"):
        if member.guild_permissions.administrator:
            embed = discord.Embed(
                title="Error!",
                description="User has Admin permissions.",
                color=0xE02B2B
            )
            await context.send(embed=embed)
        else:
            try:
                await member.kick(reason=reason)
                embed = discord.Embed(
                    title="User Kicked!",
                    description=f"**{member}** was kicked by **{context.message.author}**!",
                    color=0x42F56C
                )
                embed.add_field(
                    name="Reason:",
                    value=reason
                )
                await context.send(embed=embed)
                try:
                    await member.send(
                        f"You were kicked by **{context.message.author}**!\nReason: {reason}"
                    )
                except:
                    pass
            except:
                embed = discord.Embed(
                    title="Error!",
                    description="An error occurred while trying to kick the user. Make sure my role is above the role of the user you want to kick.",
                    color=0xE02B2B
                )
                await context.message.channel.send(embed=embed)
        

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban(self, context, member: discord.Member, *, reason="Not specified"):
        try:
            if member.guild_permissions.administrator:
                embed = discord.Embed(
                    title="Error!",
                    description="User has Admin permissions.",
                    color=0xE02B2B
                )
                await context.send(embed=embed)
            else:
                await member.ban(reason=reason)
                embed = discord.Embed(
                    title="User Banned!",
                    description=f"**{member}** was banned by **{context.message.author}**!",
                    color=0x42F56C
                )
                embed.add_field(
                    name="Reason:",
                    value=reason
                )
                await context.send(embed=embed)
                await member.send(f"You were banned by **{context.message.author}**!\nReason: {reason}")
        except:
            embed = discord.Embed(
                title="Error!",
                description="An error occurred while trying to ban the user. Make sure my role is above the role of the user you want to ban.",
                color=0xE02B2B
            )
            await context.send(embed=embed)

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
