import random

import discord
from discord.commands import slash_command
from discord.ext import commands


class RaffleView(discord.ui.View):
    def __init__(self, host):
        self.host = host
        self.contestants: list[discord.User | discord.Member | None] = []
        super().__init__()

    @discord.ui.button(label="Enter the raffle!", style=discord.ButtonStyle.primary, emoji="🎫")
    async def enter_contestant_callback(self, button, interaction: discord.Interaction):
        if interaction.user not in self.contestants:
            self.contestants.append(interaction.user)
            current_contestants = [c.display_name for c in self.contestants]  # type: ignore
            await interaction.message.edit(content=f"Current contestants: {', '.join(current_contestants)}")  # type: ignore
        await interaction.response.defer()

    @discord.ui.button(label="Pick a winner!")
    async def pick_winner_callback(self, button, interaction: discord.Interaction):
        if self.host != interaction.user:
            await interaction.response.send_message(
                "Only the creator of the raffle can decide when to call a winner",
                ephemeral=True,
            )
            return

        if not self.contestants:
            await interaction.message.edit(  # type: ignore
                embed=discord.Embed(
                    title="No one entered the raffle :^)",
                    color=discord.Color.greyple(),
                ),
                view=None,
            )
            return

        winner = random.choice(self.contestants)
        await interaction.message.edit(  # type: ignore
            embed=discord.Embed(
                title=winner.display_name,  # type: ignore
                description="is the winner! 🎉",
                color=discord.Color.blurple(),
            ),
            view=None,
        )


class Raffle(commands.Cog, name="Raffle"):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="raffle")
    async def raffle(self, ctx: discord.ApplicationContext):
        """Pick a random winner from those who entered"""
        await ctx.respond("A raffle has started!", view=RaffleView(host=ctx.author))


def setup(bot):
    bot.add_cog(Raffle(bot))
