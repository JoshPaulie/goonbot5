import random

import discord
from discord.commands import slash_command, user_command
from discord.ext import commands
from goonbot import GoonBot
from util.general.wni import snide_remarks


class General(commands.Cog):
    """General purpose commands"""

    def __init__(self, bot: GoonBot):
        self.bot = bot

    @slash_command()
    async def pfp(self, ctx: discord.ApplicationContext):
        """Profile picture grabber"""
        embed = discord.Embed(color=discord.Color.blurple())
        embed.title = "/pfp has moved!"
        embed.description = "Right click any user (including yourself)\nSelect Apps > Profile Picture"
        await ctx.respond(embed=embed, ephemeral=True)

    @user_command(name="Profile Picture")
    async def pfp_user_command(self, ctx: discord.ApplicationContext, member: discord.Member):
        pfp_url = member.display_avatar.url
        embed = discord.Embed(title=member.display_name, url=pfp_url)
        embed.set_image(url=pfp_url)
        embed.color = discord.Color.blurple()
        await ctx.respond(embed=embed)

    @slash_command()
    async def wni(self, ctx: discord.ApplicationContext):
        """Make it known that you would have enjoyed whatever they're doing (without you)"""
        embed = discord.Embed(title="Wow, no invite?", color=discord.Color.blurple())
        embed.description = random.choice(snide_remarks)
        await ctx.respond(embed=embed)

    @slash_command()
    async def coinflip(self, ctx: discord.ApplicationContext):
        """Gives you heads or tails"""
        coin = random.choice(["Heads", "Tails"])
        await ctx.respond(embed=discord.Embed(title=coin, color=discord.Color.blurple()))


def setup(bot):
    bot.add_cog(General(bot))
