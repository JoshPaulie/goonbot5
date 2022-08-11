from collections.abc import Iterator
from pathlib import Path

import discord


def collect_cogs() -> Iterator[str]:
    """
    Yields files names from cogs/ folders, formatted so py-cord can load them into the bot as extensions.
    cogs/general.py -> cogs.general
    """
    files = Path("cogs").rglob("*.py")
    for file in files:
        if "__init__" not in file.name:
            yield file.as_posix()[:-3].replace("/", ".")


def load_cogs(bot: discord.Bot):
    """
    Hacky way to load cogs into bot without explicitly specifying new cogs.
    """
    for cog in collect_cogs():
        bot.load_extension(cog, store=False)
