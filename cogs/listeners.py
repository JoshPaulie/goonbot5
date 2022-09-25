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

    @commands.Cog.listener(name="on_application_command")
    async def on_application_command_listener(self, ctx: discord.ApplicationContext):
        """Fires after an app command is used."""
        self.bot.console.log(f"{ctx.author.name} used {ctx.command.qualified_name}")  # type: ignore


def setup(bot):
    bot.add_cog(Listeners(bot))
