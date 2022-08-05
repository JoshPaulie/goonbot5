import os

from dotenv import load_dotenv

from goonbot import GoonBot

load_dotenv(".env")
goonbot = GoonBot()


goonbot.run(os.getenv("DISCORD"))
