import random

import discord
from discord.commands import Option, slash_command
from discord.ext import commands
from goonbot import GoonBot


class General(commands.Cog):
    """General purpose commands"""

    def __init__(self, bot: GoonBot):
        self.bot = bot

    @slash_command()
    async def pfp(self, ctx: discord.ApplicationContext, user: Option(discord.Member, "Pick a goon to fetch pfp") = None):  # type: ignore
        """Profile picture grabber"""
        selected_user = user if user else ctx.author
        pfp_url = selected_user.display_avatar.url  # type: ignore

        embed = discord.Embed(color=discord.Color.blurple())
        embed.set_author(name=f"{selected_user.name} 📸", url=pfp_url)  # type: ignore
        embed.set_image(url=pfp_url)
        await ctx.respond(embed=embed)

    @slash_command()
    async def wni(self, ctx: discord.ApplicationContext):
        """Make it known that you would have enjoyed whatever they're doing (without you)"""
        complaint = random.choice(
            [
                "Wow, no invite?",
                "WOW..no invite?",
                "My invite must have gotten lost in the mail",
                "Wow no invite?",
                "WOW. NOT INVITED, NOT SURPRISED.",
                "WOW. NO INVITE, NOT SURPRISED.",
                "come on man not cool",
                "i thought we were friends",
                "guess ill hangout here... alone... again",
                "hey, come on! I like darts too",
            ]
        )
        await ctx.respond(embed=discord.Embed(title=complaint, color=discord.Color.blurple()))

    @slash_command()
    async def coinflip(self, ctx: discord.ApplicationContext):
        """Gives you heads or tails"""
        coin = random.choice(["Heads", "Tails"])
        await ctx.respond(embed=discord.Embed(title=coin, color=discord.Color.blurple()))


def setup(bot):
    bot.add_cog(General(bot))
