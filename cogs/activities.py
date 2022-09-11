import random

from discord.ext import commands, tasks
from goonbot import GoonBot
from util.activities import goonbot_activities


class Activities(commands.Cog, name="Activities"):
    def __init__(self, bot: GoonBot):
        self.bot = bot
        self.set_activity.start()

        # Set an initial activity, incase the set_activity() rolls to not change the activity
        self.bot.activity = random.choice(goonbot_activities)

    def cog_unload(self):
        self.set_activity.cancel()

    @tasks.loop(minutes=15)
    async def set_activity(self):
        """33% chance of changing activity every 15 minutes"""
        if random.randint(1, 3) == 1:
            await self.bot.change_presence(activity=random.choice(goonbot_activities))

    @set_activity.before_loop
    async def before_set_activity(self):
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(Activities(bot))
