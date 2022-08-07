import random

import discord
from discord.commands import slash_command
from discord.ext import commands


class Rat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.unused_rats = self.rat_images()
        self.used_rats = []

    @staticmethod
    def rat_images() -> list:
        """Turn rat URLs textfile into list of rat URLs"""
        with open("util/txt/rats.txt", encoding="utf-8") as links:
            unused_rats = links.read().splitlines()
            return unused_rats

    def check_rat_capacity(self):
        if len(self.unused_rats) == 0:
            self.unused_rats = self.used_rats
            self.used_rats = []

    def pick_rat(self) -> str:
        """Returns a random rat URL from the"""
        chosen_rat = random.choice(self.unused_rats)
        self.unused_rats.remove(chosen_rat)
        self.used_rats.append(chosen_rat)
        return chosen_rat

    @slash_command()
    async def rat(self, ctx: discord.ApplicationContext):
        """Send an a random image from a curated list of rodents 🐀"""
        rat = self.pick_rat()
        embed = discord.Embed(title="Rat", color=discord.Color.blurple()).set_image(url=rat)
        await ctx.respond(embed=embed)  # type: ignore
        self.check_rat_capacity()


def setup(bot):
    bot.add_cog(Rat(bot))
