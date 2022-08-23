import random

import discord
from discord.commands import slash_command, user_command
from discord.ext import commands
from goonbot import GoonBot


class Affirmations(commands.Cog):
    def __init__(self, bot: GoonBot):
        self.bot = bot

    @slash_command()
    async def ily(self, ctx: discord.ApplicationContext):
        """Tell someone you loved them! Or can you?"""
        embed = discord.Embed(color=discord.Color.blurple())
        embed.title = "/ily has moved!"
        embed.description = "Right click any user (including yourself)\nSelect Apps > I love you!"
        await ctx.respond(embed=embed, ephemeral=True)

    @user_command(name="I love you!")
    async def ily_user_command(self, ctx: discord.ApplicationContext, member: discord.Member):
        """Tell someone you love them!"""
        emotes = random.choice(["😍", "😘", "🥰", "🤩", "🤗", "❤", "💕", "💞", "🖤"])
        await ctx.respond(f"{ctx.author.display_name} loves you, <@{member.id}>! {emotes}")  # type: ignore


def setup(bot):
    bot.add_cog(Affirmations(bot))
