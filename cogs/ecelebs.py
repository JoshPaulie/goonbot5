import discord
from discord.commands import slash_command
from discord.ext import commands
from goonbot import GoonBot
from util.ecelebs.views import eCelebButtonView


class eCelebs(commands.Cog):
    def __init__(self, bot: GoonBot):
        self.bot = bot

    @slash_command()
    async def thebausffs(self, ctx: discord.ApplicationContext):
        await ctx.respond(view=eCelebButtonView(youtube="UCu7ODDeIZ4x1rJwM1LCVL8w", twitch="thebausffs"))

    @slash_command()
    async def campbell(self, ctx: discord.ApplicationContext):
        await ctx.respond(view=eCelebButtonView(youtube="UCF9IOB2TExg3QIBupFtBDxg"))

    @slash_command()
    async def synapse(self, ctx: discord.ApplicationContext):
        await ctx.respond(view=eCelebButtonView(youtube="UCVw8WSz1c_cazwOA0Yk_P_w"))

    @slash_command()
    async def happy_hob(self, ctx: discord.ApplicationContext):
        await ctx.respond(view=eCelebButtonView(youtube="UC0E1n0GRgBW5gR7y7H9TjZQ", twitch="the_happy_hob"))

    @slash_command()
    async def dangheesling(self, ctx: discord.ApplicationContext):
        await ctx.respond(view=eCelebButtonView(youtube="UCVHtlynIkgJxxXrisVUZlYQ", twitch="dangheesling"))

    @slash_command()
    async def northernlion(self, ctx: discord.ApplicationContext):
        await ctx.respond(view=eCelebButtonView(youtube="UC3tNpTOHsTnkmbwztCs30sA", twitch="northernlion"))

    @slash_command()
    async def squeex(self, ctx: discord.ApplicationContext):
        await ctx.respond(view=eCelebButtonView(youtube="UCSnd_UHkXW7uBpjHz4qIq5Q", twitch="squeex"))

    @slash_command()
    async def fascinating_horror(self, ctx: discord.ApplicationContext):
        await ctx.respond(view=eCelebButtonView(youtube="UCFXad0mx4WxY1fXdbvtg0CQ"))


def setup(bot):
    bot.add_cog(eCelebs(bot))
