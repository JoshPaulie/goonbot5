import random

import discord
from discord.ext import commands, tasks
from goonbot import GoonBot

LISTENING = [
    "Owl City",
    "Enemy (J.I.D. Verse Only)",
    "your thoughts",
    "Dunkin Darius (10H Loop)",
]

PLAYING = [
    "dead",
    "chess",
    "wild rift",
    "toontown",
    "you",
    "adventure quest",
    "tribal wars",
    "Spore",
    "Endless Online",
]

WATCHING = [
    "Arcane: Season 2",
    "Camp Rock!",
    f"Harry Potter Book 7 Part {random.randint(1, 100)}",
    "'Justin W' Videos",
    "'Chunk Crunkland' Videos",
]

goonbot_activities = [
    discord.Activity(type=discord.ActivityType.playing, name=random.choice(PLAYING)),
    discord.Activity(type=discord.ActivityType.listening, name=random.choice(LISTENING)),
    discord.Activity(type=discord.ActivityType.watching, name=random.choice(WATCHING)),
]


class Activities(commands.Cog, name="Activities"):
    def __init__(self, bot: GoonBot):
        self.bot = bot
        self.set_activity.start()
        self.bot.activity = random.choice(goonbot_activities)

    def cog_unload(self):
        self.set_activity.cancel()

    @tasks.loop(minutes=15)
    async def set_activity(self):
        if random.randint(1, 3) == 1:
            await self.bot.change_presence(activity=random.choice(goonbot_activities))

    @set_activity.before_loop
    async def before_set_activity(self):
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(Activities(bot))
