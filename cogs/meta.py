import random

import discord
from discord.commands import SlashCommandGroup
from discord.ext import commands
from goonbot import GoonBot
from util.meta.modals import SuggestionModal


class Meta(commands.Cog):
    """Commands related to the bot itself"""

    def __init__(self, bot: GoonBot):
        self.bot = bot

    meta_group = SlashCommandGroup("meta", "Commands related to the bot itself")

    @meta_group.command()
    async def ping(self, ctx: discord.ApplicationContext):
        """Check the latency of goonbot"""
        latency = f"{round(self.bot.latency * 1000)}ms"
        await ctx.respond(embed=discord.Embed(title=latency, color=discord.Color.blurple()))

    @meta_group.command()
    async def uptime(self, ctx: discord.ApplicationContext):
        """Check how long the goonbot has been online"""
        uptime = self.bot.startup.humanize()
        await ctx.respond(
            embed=discord.Embed(
                title=f"{self.bot.user.display_name} was last restarted...",  # type: ignore
                description=uptime,
                color=discord.Color.blurple(),
            )
        )

    @meta_group.command()
    async def suggestion(self, ctx: discord.ApplicationContext):
        """Make a suggest for goonbot!"""
        modal = SuggestionModal(title="Make a suggestion")
        await ctx.send_modal(modal)

    @meta_group.command()
    async def about(self, ctx: discord.ApplicationContext):
        """About goonbot"""
        embed = discord.Embed()
        embed.color = discord.Color.blurple()
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)  # type: ignore
        embed.title = "About Goonbot 5"
        embed.description = "Goonbot 5 is yet another annual iteration of our favorite spyware"
        embed.add_field(
            name="GitHub",
            value="https://github.com/JoshPaulie/goonbot5",
            inline=False,
        )
        embed.add_field(
            name="Total Commands",
            value=str(len(self.bot.commands)),
            inline=False,
        )
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Meta(bot))
