import arrow
import discord
import pyyoutube
import twitch
from keys import GOOGLE, TWITCH_CLIENT_ID, TWITCH_CLIENT_SECRET


class eCelebButtonView(discord.ui.View):
    def __init__(
        self,
        twitch: str | None = None,
        youtube: str | None = None,
    ):
        self.twitch = twitch
        self.youtube = youtube
        super().__init__()

        self.children[0].disabled = True if self.twitch is None else False  # type: ignore
        self.children[1].disabled = True if self.youtube is None else False  # type: ignore

    @discord.ui.button(label="Twitch", style=discord.ButtonStyle.primary)
    async def twitch_button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        ttv = twitch.Helix(TWITCH_CLIENT_ID, TWITCH_CLIENT_SECRET)
        eCeleb_twitch = ttv.user(self.twitch)  # type: ignore

        twitch_embed = discord.Embed()

        if eCeleb_twitch is None:
            await interaction.response.send_message(
                embed=discord.Embed(
                    title="User could not be found.",
                    description="_Were they banned? Or a name change?_",
                    color=discord.Color.brand_red(),
                )
            )
            return 0

        if eCeleb_twitch.is_live:
            twitch_embed.title = f"{self.twitch} is live!"
            twitch_embed.description = eCeleb_twitch.stream.title
            twitch_embed.set_footer(text=f"Began {arrow.get(eCeleb_twitch.stream.started_at).humanize()}")
            twitch_embed.set_thumbnail(url=eCeleb_twitch.profile_image_url)
        else:
            twitch_embed.title = f"{eCeleb_twitch.display_name} is offline 😌"
            twitch_embed.set_thumbnail(url=eCeleb_twitch.offline_image_url)
            twitch_embed.color = discord.Color.light_grey()

        await interaction.response.send_message(embed=twitch_embed)

    @discord.ui.button(label="YouTube", style=discord.ButtonStyle.primary)
    async def youtube_button_callback(self, button, interaction: discord.Interaction):
        yt = pyyoutube.Api(api_key=GOOGLE)

        channel_info = yt.get_channel_info(channel_id=self.youtube)
        uploads_playlist_id = channel_info.items[0].contentDetails.relatedPlaylists.uploads  # type: ignore
        playlist_items = yt.get_playlist_items(playlist_id=uploads_playlist_id, count=1)  # type: ignore
        lastest_upload_id = playlist_items.items[0].contentDetails.videoId  # type: ignore
        lastest_upload_url = f"https://www.youtube.com/watch?v={lastest_upload_id}"

        await interaction.response.send_message(content=lastest_upload_url)
