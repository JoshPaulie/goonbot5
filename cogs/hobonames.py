import random

import discord
from discord.commands import slash_command
from discord.ext import commands
from goonbot import GoonBot


class HoboNames(commands.Cog):
    def __init__(self, bot: GoonBot):
        self.bot = bot
        self.usernames = self.get_usernames()

    @staticmethod
    def get_usernames() -> list:
        with open("util/hobonames/usernames.txt", encoding="utf-8") as usernames:
            usernames = usernames.read().splitlines()
            usernames = [name for name in usernames if "//" not in name]
            return usernames

    @slash_command()
    async def username(self, ctx: discord.ApplicationContext):
        """Randomly pick a custom username, written by A_Toxic_Hobo"""
        await ctx.respond(
            embed=discord.Embed(
                title=random.choice(self.usernames),
                color=discord.Color.blurple(),
            )
        )


def setup(bot):
    bot.add_cog(HoboNames(bot))
