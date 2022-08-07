#!.venv/Scripts/python.exe
"""Entry point to bot."""
import os

from dotenv import load_dotenv

from goonbot import GoonBot

load_dotenv(".env")

if __name__ == "__main__":
    goonbot = GoonBot()
    goonbot.console.rule("goonbot5")
    goonbot.console.log("Starting... ⚙")
    goonbot.run(os.getenv("DISCORD"))
