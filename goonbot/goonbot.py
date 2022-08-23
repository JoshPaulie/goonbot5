import random

import arrow
import discord
from rich.console import Console

from .cog_management import collect_cogs, load_cogs

STATUSES = ["dead", "chess", "wild rift", "toontown", "you"]


class GoonBot(discord.Bot):
    """
    Goonbot5 instance
    """

    def __init__(self):
        super().__init__(
            intents=discord.Intents(members=True, messages=True, guilds=True, bans=True),
            owner_ids=[177131156028784640],
            debug_guilds=[510865274594131968],
            activity=discord.Activity(type=discord.ActivityType.playing, name=random.choice(STATUSES)),
        )

        collect_cogs()
        load_cogs(self)

        self.startup = arrow.now()
        self.console = Console()

    async def on_ready(self):
        """Overwrites default on_ready"""
        self.console.log(f"{self.user.name} has logged in 👍")  # type: ignore

    async def on_application_command(self, ctx: discord.ApplicationContext):
        """Overwrites default on_application_command, acting as a console log for who used what commands, when."""
        self.console.log(f"{ctx.author.name} used {ctx.command.qualified_name}")  # type: ignore
