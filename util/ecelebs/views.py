import arrow
import discord
import pyyoutube
import twitch
from keys import GOOGLE, TWITCH_CLIENT_ID, TWITCH_CLIENT_SECRET

"""

TODO / BRAINSTORMING

- Add eceleb commands programagically ✨
- Make dataclass that holds eceleb name and social handle(s)
- Loop over list of these 👆 dataclasses, adding them each as a new command
- Each command writes its own description based on what socials are passed
- If only 1/2 of the socials are provided, send the one instead of view

"""


def check_twitch_live(twitch_username: str) -> discord.Embed:
    ttv = twitch.Helix(TWITCH_CLIENT_ID, TWITCH_CLIENT_SECRET)
    eCeleb_twitch = ttv.user(self.twitch_username)  # type: ignore

    twitch_embed = discord.Embed()

    if eCeleb_twitch is None:
        twitch_embed.title = f"{twitch_username} could not be found."
        twitch_embed.description = "_Were they banned? Or a name change?_"
        twitch_embed.color = discord.Color.brand_red()
        return twitch_embed

    if eCeleb_twitch.is_live:
        twitch_embed.url = f"https://www.twitch.tv/{twitch_username}"
        twitch_embed.title = f"{twitch_username} is live!"
        twitch_embed.description = eCeleb_twitch.stream.title
        twitch_embed.set_footer(text=f"Began {arrow.get(eCeleb_twitch.stream.started_at).humanize()}")
        twitch_embed.set_thumbnail(url=eCeleb_twitch.profile_image_url)
        twitch_embed.color = discord.Color.brand_green()
    else:
        twitch_embed.title = f"{eCeleb_twitch.display_name} is offline 😌"
        twitch_embed.set_thumbnail(url=eCeleb_twitch.offline_image_url)
        twitch_embed.color = discord.Color.light_grey()

    return twitch_embed


def get_latest_youtube_video_url(youtube_channel_id: str) -> str:
    yt = pyyoutube.Api(api_key=GOOGLE)

    channel_info = yt.get_channel_info(channel_id=youtube_channel_id)
    uploads_playlist_id = channel_info.items[0].contentDetails.relatedPlaylists.uploads  # type: ignore
    playlist_items = yt.get_playlist_items(playlist_id=uploads_playlist_id, count=1)  # type: ignore
    lastest_upload_id = playlist_items.items[0].contentDetails.videoId  # type: ignore
    lastest_upload_url = f"https://www.youtube.com/watch?v={lastest_upload_id}"

    return lastest_upload_url


class eCelebView(discord.ui.View):
    def __init__(
        self,
        twitch_username: str | None = None,
        youtube_channel_id: str | None = None,
    ):
        self.twitch_username = twitch_username
        self.youtube_channel_id = youtube_channel_id
        super().__init__()

        twitch_button = discord.ui.Button(label="Twitch", style=discord.ButtonStyle.primary, emoji="🎥")
        twitch_button.callback = self.twitch_button_callback
        youtube_button = discord.ui.Button(label="YouTube", style=discord.ButtonStyle.primary, emoji="📺")
        youtube_button.callback = self.youtube_button_callback

        if self.twitch_username:
            self.add_item(twitch_button)

        if self.youtube_channel_id:
            self.add_item(youtube_button)

    async def twitch_button_callback(self, interaction: discord.Interaction):
        if self.twitch_username:
            twitch_embed = check_twitch_live(self.twitch_username)
            # ? This cannot be interaction.edit_original_message(). Not sure why, don't care right now
            await interaction.message.edit(content=twitch_embed, view=None)  # type: ignore

    async def youtube_button_callback(self, interaction: discord.Interaction):
        if self.youtube_channel_id:
            lastest_upload_url = get_latest_youtube_video_url(self.youtube_channel_id)
            # ? This cannot be interaction.edit_original_message(). Not sure why, don't care right now
            await interaction.message.edit(content=lastest_upload_url, view=None)  # type: ignore
