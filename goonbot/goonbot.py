import random

import arrow
import discord
from pymongo.errors import DuplicateKeyError
from rich.console import Console

from .cog_management import collect_cogs, load_cogs
from .mongo_db import db


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
            owner_ids=[
                177131156028784640,  # Bexli
            ],
            debug_guilds=[
                510865274594131968,  # Debug guild
                177125557954281472,  # g00n guild
            ],
        )

        collect_cogs()
        load_cogs(self)

        self.startup = arrow.now()
        self.console = Console(log_time_format="[%b %d, %y @ %H:%M:%S]")
        self.db = db

    async def on_ready(self):
        """Overwrites default on_ready"""
        self.console.log(f"{self.user.name} has logged in 👍")  # type: ignore

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
        """Returns a user's 'tokens' document"""
        # Disgustingly hacky way to make sure user has a token document.
        try:
            await self.tokens.insert_one({"_id": user.id, "coins": 10})
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
