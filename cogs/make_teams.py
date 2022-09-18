import random
from typing import Any

import discord
from discord.commands import slash_command
from discord.ext import commands
from goonbot import GoonBot


class MakeTeams(commands.Cog, name="Make Teams"):
    def __init__(self, bot: GoonBot):
        self.bot = bot

    @slash_command()
    async def maketeams(self, ctx: discord.ApplicationContext):
        """Makes 2 teams out of whoever is in goonHQ"""
        goon_hq = self.bot.get_channel(177125557954281473)
        currently_in = [m.name for m in goon_hq.members]  # type: ignore
        random.shuffle(currently_in)

        team_1 = currently_in[: len(currently_in) // 2]
        team_2 = currently_in[len(currently_in) // 2 :]

        teams_embed = discord.Embed(color=discord.Color.blurple())
        teams_embed.add_field(name="Team 1", value="\n".join(team_1), inline=True)
        teams_embed.add_field(name="Team 2", value="\n".join(team_2), inline=True)
        if len(currently_in) % 2 != 0:
            teams_embed.set_footer(
                text="Because there was an uneven number of players, Team 2 will have one extra player"
            )
        await ctx.respond(embed=teams_embed)  # type: ignore


def setup(bot):
    bot.add_cog(MakeTeams(bot))
