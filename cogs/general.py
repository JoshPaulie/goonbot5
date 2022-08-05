import discord
from discord.commands import slash_command
from discord.ext import commands


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def gb5(self, ctx: discord.ApplicationContext):
        """Dummy command"""
        await ctx.send("YAYY")


def setup(bot):
    bot.add_cog(General(bot))
