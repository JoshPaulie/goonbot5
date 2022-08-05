import discord
from discord.commands import slash_command


class GoonBot(discord.Bot):
    async def on_ready(self):
        print(f"{self.user} has logged in")

    @slash_command()
    async def ping(self, ctx):
        await ctx.respond("Pong!")
