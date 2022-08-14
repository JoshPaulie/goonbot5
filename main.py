#!.venv/Scripts/python.exe
"""Entry point to bot."""
from goonbot import GoonBot
from keys import DISCORD

if __name__ == "__main__":
    goonbot = GoonBot()
    goonbot.console.rule("goonbot5")
    goonbot.console.log("Starting... ⚙")
    goonbot.run(DISCORD)
