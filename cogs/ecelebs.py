from dataclasses import dataclass

import discord
from discord.ext import commands
from goonbot import GoonBot
from util.ecelebs.views import check_twitch_live, eCelebView, get_latest_youtube_video_url


@dataclass
class eCeleb:
    name: str
    twitch_username: str | None = None
    youtube_channel_id: str | None = None


eCelebs = [
    eCeleb(
        "thebausffs",
        twitch_username="thebausffs",
        youtube_channel_id="UCu7ODDeIZ4x1rJwM1LCVL8w",
    ),
]


async def both_socials_callback(ctx: discord.ApplicationContext):
    await ctx.respond(
        view=eCelebView(
            youtube_channel_id=eCeleb.youtube_channel_id,
            twitch_username=eCeleb.twitch_username,
        )
    )


async def only_twitch_callback(ctx: discord.ApplicationContext):
    await ctx.respond(embed=check_twitch_live(eCeleb.twitch_username))  # type: ignore


async def only_youtube_callback(ctx: discord.ApplicationContext):
    await ctx.respond(get_latest_youtube_video_url(eCeleb.youtube_channel_id))  # type: ignore


class eCelebsLinkCommands(commands.Cog):
    def __init__(self, bot: GoonBot):
        self.bot = bot

        for eCeleb in eCelebs:
            if all([eCeleb.twitch_username, eCeleb.youtube_channel_id]):

                eCeleb_command = discord.SlashCommand(both_socials_callback)
                eCeleb_command.name = eCeleb.name
                eCeleb_command.description = (
                    f"Check if {eCeleb.name} is live on TTV, or check their latest video on YT!"
                )

            elif eCeleb.twitch_username:

                eCeleb_command = discord.SlashCommand(only_twitch_callback)
                eCeleb_command.name = eCeleb.name
                eCeleb_command.description = f"Check if {eCeleb.name} is live on TTV!"
            else:

                eCeleb_command = discord.SlashCommand(only_youtube_callback)
                eCeleb_command.name = eCeleb.name
                eCeleb_command.description = f"Check {eCeleb.name}'s latest video on YT!"

            self.bot.add_application_command(eCeleb_command)

    # @slash_command()
    # async def thebausffs(self, ctx: discord.ApplicationContext):
    #     await ctx.respond(
    #         view=eCelebView(youtube_channel_id="UCu7ODDeIZ4x1rJwM1LCVL8w", twitch_username="thebausffs")
    #     )

    # @slash_command()
    # async def campbell(self, ctx: discord.ApplicationContext):
    #     await ctx.respond(view=eCelebView(youtube_channel_id="UCF9IOB2TExg3QIBupFtBDxg"))

    # @slash_command()
    # async def synapse(self, ctx: discord.ApplicationContext):
    #     await ctx.respond(view=eCelebView(youtube_channel_id="UCVw8WSz1c_cazwOA0Yk_P_w"))

    # @slash_command()
    # async def happy_hob(self, ctx: discord.ApplicationContext):
    #     await ctx.respond(
    #         view=eCelebView(youtube_channel_id="UC0E1n0GRgBW5gR7y7H9TjZQ", twitch_username="the_happy_hob")
    #     )

    # @slash_command()
    # async def dangheesling(self, ctx: discord.ApplicationContext):
    #     await ctx.respond(
    #         view=eCelebView(youtube_channel_id="UCVHtlynIkgJxxXrisVUZlYQ", twitch_username="dangheesling")
    #     )

    # @slash_command()
    # async def northernlion(self, ctx: discord.ApplicationContext):
    #     await ctx.respond(
    #         view=eCelebView(youtube_channel_id="UC3tNpTOHsTnkmbwztCs30sA", twitch_username="northernlion")
    #     )

    # @slash_command()
    # async def squeex(self, ctx: discord.ApplicationContext):
    #     await ctx.respond(
    #         view=eCelebView(youtube_channel_id="UCSnd_UHkXW7uBpjHz4qIq5Q", twitch_username="squeex")
    #     )

    # @slash_command()
    # async def fascinating_horror(self, ctx: discord.ApplicationContext):
    #     await ctx.respond(view=eCelebView(youtube_channel_id="UCFXad0mx4WxY1fXdbvtg0CQ"))

    # @slash_command()
    # async def settledrs(self, ctx: discord.ApplicationContext):
    #     await ctx.respond(view=eCelebView(youtube_channel_id="UCs-w7E2HZWwXmjt9RTvBB_A"))


def setup(bot):
    bot.add_cog(eCelebsLinkCommands(bot))
