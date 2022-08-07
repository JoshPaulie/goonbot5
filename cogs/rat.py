import random

import discord
from discord.commands import slash_command
from discord.ext import commands


class Rat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.rats = self.get_rat_images()

    @staticmethod
    def get_rat_images() -> list:
        """Turn rat URLs textfile into list of rat URLs"""
        with open("util/txt/rats.txt", encoding="utf-8") as links:
            rats = links.read().splitlines()
            return rats

    def check_rat_capacity(self):
        if len(self.rats) == 0:
            self.rats = self.get_rat_images()

    def pick_rat(self) -> str:
        """Returns a random rat URL from the in-memory list, as well as removing it from the list."""
        chosen_rat = random.choice(self.rats)
        self.rats.remove(chosen_rat)
        self.check_rat_capacity()
        return chosen_rat

    @slash_command()
    async def rat(self, ctx: discord.ApplicationContext):
        """Send an a random image from a curated list of rodents 🐀"""
        rat = self.pick_rat()
        embed = discord.Embed(color=discord.Color.blurple()).set_image(url=rat)
        await ctx.respond(embed=embed)  # type: ignore


def setup(bot):
    bot.add_cog(Rat(bot))
