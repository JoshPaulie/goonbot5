import asyncio
import random
from string import punctuation

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

    @slash_command()
    @discord.option(
        "minutes",
        description="Enter timer duration (minutes)",
        min_value=0,
        max_value=120,
        default=0,
    )
    @discord.option(
        "seconds",
        description="Enter timer duration (seconds)",
        min_value=0,
        max_value=120,
        default=0,
    )
    async def timer(self, ctx: discord.ApplicationContext, minutes: int, seconds: int):
        """Set a timer"""
        await ctx.respond(
            embed=discord.Embed(
                title="Timer started!",
                description=f"{ctx.author.display_name} set a timer for {minutes}m {seconds}s",  # type: ignore
                color=discord.Color.greyple(),
            )
        )
        await asyncio.sleep((minutes * 60) + seconds)
        await ctx.edit(
            embed=discord.Embed(
                title=f"{ctx.author.display_name}, your timer has ended!",  # type: ignore
                color=discord.Color.blurple(),
            )
        )  # type: ignore

    @slash_command(name="ag")
    async def ag(self, ctx: discord.ApplicationContext, phrase: str):
        """Acronym Generator"""
        for char in phrase:
            if char in punctuation:
                await ctx.respond(
                    embed=discord.Embed(title="No punctuation! 😡", color=discord.Color.blurple()),
                    ephemeral=True,
                )
                return

        await ctx.respond(
            embed=discord.Embed(
                title=f"{''.join([word[0].upper() for word in phrase.split()])}",
                description=f"*{phrase}*",
                color=discord.Color.blurple(),
            )
        )

    # TODO Raffle Command

    # TODO Voting Command
    # Modals?


def setup(bot):
    bot.add_cog(General(bot))
