import discord
from rich.console import Console

from .cog_management import collect_cogs, load_cogs


class GoonBot(discord.Bot):
    """Goonbot instance"""

    def __init__(self):
        super().__init__(
            intents=discord.Intents(members=True, messages=True, guilds=True, bans=True),
            owner_ids=[177131156028784640],
            debug_guilds=[510865274594131968],
            activity=discord.Activity(type=discord.ActivityType.playing, name="👨‍🚀"),
        )

        collect_cogs()
        load_cogs(self)
        self.console = Console()

    async def on_ready(self):
        """Prints if bot successfully comes online"""
        self.console.log(f"{self.user.name} has logged in 👍")  # type: ignore

    async def on_application_command(self, ctx: discord.ApplicationContext):
        """Prints when commands are used"""
        self.console.log(f"{ctx.author.name} used {ctx.command.qualified_name}")  # type: ignore
