import datetime
import random

import discord
from discord.commands import message_command, slash_command, user_command
from discord.ext import commands
from goonbot import GoonBot
from util.general.wie import time_of_day
from util.general.wni import snide_remarks


class General(commands.Cog):
    """General purpose commands"""

    def __init__(self, bot: GoonBot):
        self.bot = bot

    @user_command(name="📸 pfp")
    async def pfp_user_command(self, ctx: discord.ApplicationContext, member: discord.Member):
        pfp_url = member.display_avatar.url
        embed = discord.Embed(title=member.display_name, url=pfp_url)
        embed.set_image(url=pfp_url)
        embed.color = discord.Color.blurple()
        await ctx.respond(embed=embed)

    @slash_command()
    async def usercommand(self, ctx: discord.ApplicationContext):
        """Gif of how User Commands are used"""
        embed = discord.Embed(title="How to use a User Command")
        embed.set_image(url="https://i.imgur.com/Ak1nsjk.gif")
        embed.color = discord.Color.blurple()
        await ctx.respond(embed=embed)

    @slash_command()
    async def wni(self, ctx: discord.ApplicationContext):
        """Make it known that you would have enjoyed whatever they're doing (without you)"""
        embed = discord.Embed(title="Wow, no invite?", color=discord.Color.blurple())
        embed.description = random.choice(snide_remarks)
        await ctx.respond(embed=embed)

    @slash_command()
    async def wie(self, ctx: discord.ApplicationContext):
        """Make it known that you are in VC and would love to create some memories (with you)"""
        today = datetime.datetime.today()
        embed = discord.Embed(title="Where is everyone?", color=discord.Color.blurple())
        embed.description = f"It's a {today.strftime('%A')} {time_of_day(today.strftime('%H'))}!"
        await ctx.respond(embed=embed)

    @slash_command()
    async def coinflip(self, ctx: discord.ApplicationContext):
        """Gives you heads or tails"""
        coin = random.choice(["Heads", "Tails"])
        await ctx.respond(embed=discord.Embed(title=coin, color=discord.Color.blurple()))

    @slash_command(name="ag")
    async def ag(self, ctx: discord.ApplicationContext, phrase: str):
        """Acronym Generator"""
        await ctx.respond(
            embed=discord.Embed(
                title=f"{''.join([word[0].upper() for word in phrase.split()])}",
                description=f"*{phrase}*",
                color=discord.Color.blurple(),
            )
        )

    @message_command(name="Generate Acronym")
    async def ag_message_command(self, ctx: discord.ApplicationContext, message: discord.Message):
        """Acronym Generator"""
        await ctx.respond(
            embed=discord.Embed(
                title=f"{''.join([word[0].upper() for word in message.content.split()])}",
                description=f"*{message.content}*",
                color=discord.Color.blurple(),
            )
        )

    @slash_command()
    async def vtuber(self, ctx: discord.ApplicationContext):
        """Check to see if one of many vtubers are live!"""
        await ctx.respond(
            embed=discord.Embed(
                title=f"Someone is Live!", url="https://holodex.net/", color=discord.Color.brand_green()
            )
        )
        if ctx.author.id == 104488848309895168:  # type: ignore
            emote = ["🖕", "😎", "🤫"]
            await ctx.send(f"gotcha, nerd {random.choice(emote)}", delete_after=1)

    @slash_command(name="chooseforme")
    async def choose_for_me(
        self,
        ctx: discord.ApplicationContext,
        options: discord.Option(str, "Enter choices, separated by a comma"),  # type: ignore
    ):
        """Have goonbot pick from a list of choices"""
        # Todo make this into a modal with title ? :thonking:
        cleaned_options = [option.strip() for option in options.split(",")]
        embed = discord.Embed(
            title=random.choice(cleaned_options),
            description=f"*goonbot has chosen from...*\n{', '.join(cleaned_options)}",
            color=discord.Color.brand_green(),
        )
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
