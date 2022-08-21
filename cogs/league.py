import random

import discord
from discord.commands import slash_command
from discord.ext import commands
from goonbot import GoonBot


class League(commands.Cog):
    def __init__(self, bot: GoonBot):
        self.bot = bot


def setup(bot):
    bot.add_cog(League(bot))
