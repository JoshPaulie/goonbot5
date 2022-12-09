import random

import discord
from discord.ext import commands


def same(lst):
    base = lst[0]
    for item in lst:
        if base != item:
            return False
    return True


class Listeners(commands.Cog, name="listeners"):
    def __init__(self, bot):
        self.bot = bot
        self.message_queue = []

    # @commands.Cog.listener(name="on_message")
    # async def example_listener(self, message: discord.Message):
    #     """Reference listener"""
    #     print(message.content)

    @commands.Cog.listener(name="on_application_command")
    async def on_application_command_listener(self, ctx: discord.ApplicationContext):
        """Fires after an app command is used."""
        self.bot.console.log(f"{ctx.author.name} used {ctx.command.qualified_name}")  # type: ignore

    @commands.Cog.listener(name="on_message")
    async def chatting_watch(self, message: discord.Message):
        """Adds a :Chatting: reaction to anyone who posts 5 times consecutively"""
        author = message.author
        self.message_queue.append(author)

        if not same(self.message_queue):
            self.message_queue.clear()

        if len(self.message_queue) == 5:
            await message.add_reaction("<:Chatting:937413522592264272>")
            self.message_queue.clear()


def setup(bot):
    bot.add_cog(Listeners(bot))
