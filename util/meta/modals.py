import random

import discord


class AnnouncementModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Announcements", style=discord.InputTextStyle.multiline))

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            embed=discord.Embed(
                title="📣 Goonbot has been updated!",
                description=self.children[0].value,
                color=discord.Color.blurple(),
            )
        )
