import os

from dotenv import load_dotenv

from goonbot import GoonBot

load_dotenv(".env")
goonbot = GoonBot(debug_guilds=[510865274594131968])

goonbot.run(os.getenv("DISCORD"))
