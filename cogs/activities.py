import random

import discord
from discord.ext import commands, tasks
from goonbot import GoonBot

LISTENING_TO = [
    "Owl City",
    "Enemy (J.I.D. Verse Only)",
    "your thoughts",
    "Dunking Darius (10-Hour Loop)",
]

PLAYING = [
    "dead",
    "chess",
    "wild rift",
    "toontown",
    "you",
    "rs3",
    "adventure quest",
    "tribal wars",
    "Spore",
]

WATCHING = [
    "Arcane Season 2",
    "Camp Rock!",
    f"Harry Potter Book 7 Part {random.randint(1, 100)}",
]


class Activities(commands.Cog, name="Activities"):
    def __init__(self, bot: GoonBot):
        self.bot = bot
        self.set_activity.start()

    def cog_unload(self):
        self.set_activity.cancel()

    @tasks.loop(minutes=15.0)
    async def set_activity(self):
        await self.bot.change_presence(
            activity=random.choice(
                [
                    discord.Activity(type=discord.ActivityType.playing, name=random.choice(PLAYING)),
                    discord.Activity(type=discord.ActivityType.listening, name=random.choice(LISTENING_TO)),
                    discord.Activity(type=discord.ActivityType.watching, name=random.choice(WATCHING)),
                ]
            )
        )

    @set_activity.before_loop
    async def before_set_activity(self):
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(Activities(bot))
