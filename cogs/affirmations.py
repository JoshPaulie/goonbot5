import random

import discord
from discord.commands import user_command
from discord.ext import commands
from goonbot import GoonBot


class Affirmations(commands.Cog):
    def __init__(self, bot: GoonBot):
        self.bot = bot

    @user_command(name="I love you!")
    async def ily(self, ctx: discord.ApplicationContext, member: discord.Member):
        """Tell someone you love them!"""
        emotes = ["😍", "😘", "🥰", "🤩", "🤗", "❤", "💕", "💞", "🖤"]
        await ctx.respond(f"Someone loves you, <@{member.id}>! {random.choice(emotes)}")  # type: ignore


def setup(bot):
    bot.add_cog(Affirmations(bot))
