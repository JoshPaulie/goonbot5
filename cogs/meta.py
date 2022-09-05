import random

import discord
from discord.commands import SlashCommandGroup, slash_command
from discord.ext import commands
from goonbot import GoonBot


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

    @slash_command()
    async def suggest(
        self,
        ctx: discord.ApplicationContext,
        suggestion: discord.Option(str, "What feature should be implemented to goonbot?"),  # type: ignore
    ):
        """Make a suggestion for goonbot!"""
        sassy_responses = [
            "Wow! this will definitely be implemented",
            "Oh, nice idea bu-ddy!",
            "I'll think about that! 😉",
        ]

        embed = discord.Embed(title=random.choice(sassy_responses), color=discord.Color.blurple())
        embed.add_field(name=f"Suggestion", value=suggestion)  # type: ignore
        embed.set_footer(text=f"Author: {ctx.author.display_name}") # type: ignore
        await ctx.respond(embed=embed)
        await self.bot.db["suggestions"].insert_one(  # type: ignore
            dict(
                author=ctx.author.name,  # type: ignore
                suggestion=suggestion,
                open=True,
            )
        )


def setup(bot):
    bot.add_cog(Meta(bot))
