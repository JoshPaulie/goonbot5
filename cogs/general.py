import asyncio
import random
from string import punctuation

import discord
from discord.commands import message_command, slash_command, user_command
from discord.ext import commands
from goonbot import GoonBot
from util.general.wni import snide_remarks


class General(commands.Cog):
    """General purpose commands"""

    def __init__(self, bot: GoonBot):
        self.bot = bot

    @user_command(name="Profile Picture")
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
    async def raffle(self, ctx: discord.ApplicationContext):
        """Pick a random member from the server"""
        winner = random.choice(ctx.guild.members)  # type: ignore
        await ctx.respond(embed=discord.Embed(title=f"{winner.name} 🎉", color=discord.Color.blurple()))

    @user_command(name="About")
    async def about_user(self, ctx: discord.ApplicationContext, member: discord.Member):
        """about"""
        embed = discord.Embed(title=member.display_name, color=member.color)
        embed.add_field(
            name=f"Joined {ctx.guild.name}",  # type: ignore
            value=member.joined_at.strftime("%b %d %Y"),  # type: ignore
            inline=False,
        )
        embed.add_field(
            name=f"Joined Discord",  # type: ignore
            value=member.created_at.strftime("%b %d %Y"),  # type: ignore
            inline=False,
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text=f"ID: {member.id}")
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
