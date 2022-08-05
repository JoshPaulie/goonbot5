import os

import discord
from dotenv import load_dotenv

from goonbot import GoonBot

load_dotenv(".env")
intents = discord.Intents.default()
intents.members = True
goonbot = GoonBot(debug_guilds=[510865274594131968], intents=intents)


goonbot.run(os.getenv("DISCORD"))
