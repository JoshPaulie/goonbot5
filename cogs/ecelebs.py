import arrow
import discord
import twitch
from discord.commands import slash_command
from discord.ext import commands


# type: ignore
class TwitchYoutubeView(discord.ui.View):
    @discord.ui.button(label="Twitch", style=discord.ButtonStyle.primary)
    async def twitch_button_callback(self, button, interaction: discord.Interaction):
        await interaction.response.send_message(content="You clicked twitch")

    @discord.ui.button(label="YouTube", style=discord.ButtonStyle.primary)
    async def youtube_button_callback(self, button, interaction: discord.Interaction):
        await interaction.response.send_message(content="You clicked youtube")


class eCelebs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def twitch_youtube_test(self, ctx):
        await ctx.respond(view=TwitchYoutubeView())


def setup(bot):
    bot.add_cog(eCelebs(bot))
