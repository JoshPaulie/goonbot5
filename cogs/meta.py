import random

import discord
from discord.commands import SlashCommandGroup
from discord.ext import commands
from goonbot import GoonBot


class SuggestionModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="TLDR"))  # Suggestion title
        self.add_item(
            discord.ui.InputText(
                label="Tell me about it... 🍿", style=discord.InputTextStyle.long, required=False
            )
        )

    async def callback(self, interaction: discord.Interaction):
        sassy_responses = [
            "Wow! this will definitely be implemented",
            "Oh, nice idea buddy!",
            "I'll think about that!",
        ]
        embed = discord.Embed(title="Suggestion sent!", description=random.choice(sassy_responses))
        suggestion_title = self.children[0].value
        suggestion_details = self.children[1].value or "None"
        await interaction.response.send_message(embeds=[embed])
        print(suggestion_title, suggestion_details)


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
        """Check how long the bot has been online"""
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


def setup(bot):
    bot.add_cog(Meta(bot))
