import random

import discord


class SuggestionModal(discord.ui.Modal):
    """Modal used in meta.suggestion"""

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
            "Oh, nice idea bu-ddy!",
            "I'll think about that!",
        ]
        embed = discord.Embed(title="Suggestion sent!", description=random.choice(sassy_responses))
        suggestion_title = self.children[0].value
        suggestion_details = self.children[1].value or "..."
        print(f"{interaction.user.display_name} suggests {suggestion_title}: {suggestion_details}")  # type: ignore
        # await interaction.response.send_message(embed=embed)
        await interaction.response.send_message(
            embed=discord.Embed(
                title="Manually recorded 📝",
                description="I have yet to set up a database, so all suggestions are written to a text file.\n \
                    All suggestions made before the DB will be migrated",
            ),
            ephemeral=True,
        )
