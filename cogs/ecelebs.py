import discord
from discord.commands import slash_command
from discord.ext import commands
from goonbot import GoonBot
from util.ecelebs.views import eCelebView


class eCelebs(commands.Cog):
    def __init__(self, bot: GoonBot):
        self.bot = bot

    @slash_command()
    async def thebausffs(self, ctx: discord.ApplicationContext):
        await ctx.respond(
            view=eCelebView(youtube_channel_id="UCu7ODDeIZ4x1rJwM1LCVL8w", twitch_username="thebausffs")
        )

    @slash_command()
    async def campbell(self, ctx: discord.ApplicationContext):
        await ctx.respond(view=eCelebView(youtube_channel_id="UCF9IOB2TExg3QIBupFtBDxg"))

    @slash_command()
    async def synapse(self, ctx: discord.ApplicationContext):
        await ctx.respond(view=eCelebView(youtube_channel_id="UCVw8WSz1c_cazwOA0Yk_P_w"))

    @slash_command()
    async def happy_hob(self, ctx: discord.ApplicationContext):
        await ctx.respond(
            view=eCelebView(youtube_channel_id="UC0E1n0GRgBW5gR7y7H9TjZQ", twitch_username="the_happy_hob")
        )

    @slash_command()
    async def dangheesling(self, ctx: discord.ApplicationContext):
        await ctx.respond(
            view=eCelebView(youtube_channel_id="UCVHtlynIkgJxxXrisVUZlYQ", twitch_username="dangheesling")
        )

    @slash_command()
    async def northernlion(self, ctx: discord.ApplicationContext):
        await ctx.respond(
            view=eCelebView(youtube_channel_id="UC3tNpTOHsTnkmbwztCs30sA", twitch_username="northernlion")
        )

    @slash_command()
    async def squeex(self, ctx: discord.ApplicationContext):
        await ctx.respond(
            view=eCelebView(youtube_channel_id="UCSnd_UHkXW7uBpjHz4qIq5Q", twitch_username="squeex")
        )

    @slash_command()
    async def fascinating_horror(self, ctx: discord.ApplicationContext):
        await ctx.respond(view=eCelebView(youtube_channel_id="UCFXad0mx4WxY1fXdbvtg0CQ"))

    @slash_command()
    async def settledrs(self, ctx: discord.ApplicationContext):
        await ctx.respond(view=eCelebView(youtube_channel_id="UCs-w7E2HZWwXmjt9RTvBB_A"))


def setup(bot):
    bot.add_cog(eCelebs(bot))
