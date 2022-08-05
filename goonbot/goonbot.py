import discord

from .cog_management import collect_cogs, load_cogs


class GoonBot(discord.Bot):
    """Goonbot instance"""

    def __init__(self):
        super().__init__(
            intents=discord.Intents(members=True, messages=True, guilds=True, bans=True),
            owner_ids=[177131156028784640],
            debug_guilds=[510865274594131968],
            activity=discord.Activity(type=discord.ActivityType.listening, name="Dev 😙"),
        )

        collect_cogs()
        load_cogs(self)

    async def on_ready(self):
        """Prints if bot successfully comes online"""
        print(f"{self.user} has logged in")

    async def on_application_command(self, ctx: discord.ApplicationContext):
        """Prints when commands are used"""
        print(f"{ctx.author.name} used {ctx.command.qualified_name}")  # type: ignore
