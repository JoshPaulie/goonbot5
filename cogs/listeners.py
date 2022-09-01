import random

import discord
from discord.ext import commands


class Listeners(commands.Cog, name="listeners"):
    def __init__(self, bot):
        self.bot = bot

    # @commands.Cog.listener(name="on_message")
    # async def example_listener(self, message: discord.Message):
    #     """Reference listener"""
    #     print(message.content)


def setup(bot):
    bot.add_cog(Listeners(bot))
