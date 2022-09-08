import random

import arrow
import discord
from pymongo.errors import DuplicateKeyError
from rich.console import Console

from .cog_management import collect_cogs, load_cogs
from .mongo_db import db

STATUSES = ["dead", "chess", "wild rift", "toontown", "you"]


class GoonBot(discord.Bot):
    """
    Goonbot5 instance
    """

    def __init__(self):
        super().__init__(
            intents=discord.Intents(
                members=True,
                messages=True,
                guilds=True,
                bans=True,
                message_content=True,
            ),
            owner_ids=[177131156028784640],  # Bexli
            debug_guilds=[510865274594131968, 177125557954281472],  # [Debug guild, g00n guild]
            activity=discord.Activity(type=discord.ActivityType.playing, name=random.choice(STATUSES)),
        )

        collect_cogs()
        load_cogs(self)

        self.startup = arrow.now()
        self.console = Console()
        self.db = db

    async def on_ready(self):
        """Overwrites default on_ready"""
        self.console.log(f"{self.user.name} has logged in 👍")  # type: ignore

    async def on_application_command(self, ctx: discord.ApplicationContext):
        """Overwrites default on_application_command, acting as a console log for who used what commands, when."""
        self.console.log(f"{ctx.author.name} used {ctx.command.qualified_name}")  # type: ignore

    @property
    def suggestions(self):
        return self.db["suggestions"]

    @property
    def bios(self):
        return self.db["bios"]

    @property
    def tokens(self):
        return self.db["tokens"]

    async def get_tokens(self, user: discord.Member | discord.User):
        """Disgustingly hacky way to check how many of a specific token a user has.
        If user doesn't have any tokens, create a new document and give them 0 of token checked"""
        try:
            await self.tokens.insert_one({"_id": user.id})
        except DuplicateKeyError:
            pass

        user_tokens = await self.tokens.find_one({"_id": user.id})
        return user_tokens

    async def get_token_amount(self, token: str, user: discord.Member | discord.User):
        """Check to see how many of a specific token a user has"""
        user_tokens = await self.get_tokens(user)
        return user_tokens.get(token)

    async def change_token_amount(self, token: str, user: discord.Member | discord.User, change_amount: int):
        user_tokens = await self.get_tokens(user)
        await self.tokens.update_one(user_tokens, {"$inc": {"coins": change_amount}})
        return user_tokens.get(token)
