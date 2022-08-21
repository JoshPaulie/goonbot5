import arrow
import discord
import pyyoutube
import twitch
from keys import GOOGLE, TWITCH_CLIENT_ID, TWITCH_CLIENT_SECRET


class eCelebButtonView(discord.ui.View):
    def __init__(
        self,
        twitch_username: str | None = None,
        youtube_channel_id: str | None = None,
    ):
        self.twitch_username = twitch_username
        self.youtube_channel_id = youtube_channel_id
        super().__init__()

        self.children[0].disabled = True if self.twitch_username is None else False  # type: ignore
        self.children[1].disabled = True if self.youtube_channel_id is None else False  # type: ignore

    @discord.ui.button(label="Twitch", style=discord.ButtonStyle.primary, emoji="🎥")
    async def twitch_button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        ttv = twitch.Helix(TWITCH_CLIENT_ID, TWITCH_CLIENT_SECRET)
        eCeleb_twitch = ttv.user(self.twitch_username)  # type: ignore

        twitch_embed = discord.Embed()

        if eCeleb_twitch is None:
            await interaction.message.edit(  # type: ignore
                embed=discord.Embed(
                    title=f"{self.twitch_username} could not be found.",
                    description="_Were they banned? Or a name change?_",
                    color=discord.Color.brand_red(),
                )
            )
            return

        if eCeleb_twitch.is_live:
            twitch_embed.title = f"{self.twitch_username} is live!"
            twitch_embed.description = eCeleb_twitch.stream.title
            twitch_embed.set_footer(text=f"Began {arrow.get(eCeleb_twitch.stream.started_at).humanize()}")
            twitch_embed.set_thumbnail(url=eCeleb_twitch.profile_image_url)
            twitch_embed.color = discord.Color.brand_green()
        else:
            twitch_embed.title = f"{eCeleb_twitch.display_name} is offline 😌"
            twitch_embed.set_thumbnail(url=eCeleb_twitch.offline_image_url)
            twitch_embed.color = discord.Color.light_grey()

        await interaction.message.edit(embed=twitch_embed, view=None)  # type: ignore

    @discord.ui.button(label="YouTube", style=discord.ButtonStyle.primary, emoji="📺")
    async def youtube_button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        yt = pyyoutube.Api(api_key=GOOGLE)

        channel_info = yt.get_channel_info(channel_id=self.youtube_channel_id)
        uploads_playlist_id = channel_info.items[0].contentDetails.relatedPlaylists.uploads  # type: ignore
        playlist_items = yt.get_playlist_items(playlist_id=uploads_playlist_id, count=1)  # type: ignore
        lastest_upload_id = playlist_items.items[0].contentDetails.videoId  # type: ignore
        lastest_upload_url = f"https://www.youtube.com/watch?v={lastest_upload_id}"

        await interaction.message.edit(content=lastest_upload_url, view=None)  # type: ignore
