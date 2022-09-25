import random

import discord
from discord.commands import slash_command
from discord.ext import commands
from goonbot import GoonBot

goon_art = dict(
    bringe=["https://cdn.discordapp.com/attachments/531913512822243358/651997904751427624/Hudboy.png"],
    gamerword=["https://cdn.discordapp.com/attachments/531913512822243358/651997280290734101/gamer.jpg"],
    pizza=["https://cdn.discordapp.com/attachments/177125557954281472/731242309446008893/image0.jpg"],
    clown=["https://cdn.discordapp.com/attachments/177125557954281472/651996397041877006/clown_2.0.jpg"],
    ygg=[
        "https://cdn.discordapp.com/attachments/733685825379893339/756322976034586654/c00a411b-1fea-4593-b528-56cfc2dea9cf.png"
    ],
    frog=[
        "https://i.imgur.com/lqZM3sR.png",
        "https://cdn.discordapp.com/attachments/177125557954281472/814729226031726632/1614310329958.jpg",
        "https://media1.tenor.com/images/ba97a5584efb72bdfa4feeacc83ea2c2/tenor.gif",
        "https://media1.tenor.com/images/bfeaafa2ff74d740f1920174ce796ef3/tenor.gif",
    ],
    joker=["https://cdn.discordapp.com/attachments/177125557954281472/754429776571138238/lex_true_form.jpg"],
    rool=["https://media1.tenor.com/images/c071dcb215cc774f730c1630a5971fb4/tenor.gif?itemid=12340096"],
)


async def get_goon_art_names(ctx: discord.AutocompleteContext):
    return sorted([name for name in goon_art.keys() if name.startswith(ctx.value.lower())])


class Art(commands.Cog):
    def __init__(self, bot: GoonBot):
        self.bot = bot

    @staticmethod
    async def send_art_embed(ctx: discord.ApplicationContext, images: list) -> None:
        art_embed = discord.Embed()
        art_embed.set_image(url=random.choice(images))
        art_embed.set_author(name=ctx.command.name)  # type: ignore
        art_embed.color = discord.Color.blurple()
        await ctx.respond(embed=art_embed)

    @slash_command()
    async def art(
        self,
        ctx: discord.ApplicationContext,
        art_piece: discord.Option(str, "Pick some art", autocomplete=get_goon_art_names),  # type: ignore
    ):
        await self.send_art_embed(ctx, goon_art[art_piece])

    @slash_command()
    async def real(self, ctx: discord.ApplicationContext):
        """Evidence of paranormal cativity and other anomalies"""
        # Alt doc string: Anything made to be remotely realistic OR paranormal can be added here
        # It's a dumpster fire at this point ✨
        evidence = [
            "https://cdn.discordapp.com/attachments/177125557954281472/810598965190983720/1612730989587.gif",
            "https://cdn.discordapp.com/attachments/177125557954281472/938132511270240356/1643438475633.gif",
            "https://cdn.discordapp.com/attachments/177125557954281472/937579976159526942/1643578958193.gif",
            "https://cdn.discordapp.com/attachments/177125557954281472/937577902113972254/1643260137906.jpg",
            "https://cdn.discordapp.com/attachments/177125557954281472/936873848001929276/1643437992106.png",
            "https://cdn.discordapp.com/attachments/177125557954281472/902737733812895824/MATT.png",
            "https://c.tenor.com/R0_afzSWuPMAAAAd/fat-guy.gif",
            "https://c.tenor.com/Lwn2wbmAXboAAAAd/skeleton.gif",
            "https://c.tenor.com/mrAgjI8uBI4AAAAC/skeleton-dance-skeletons.gif",
            "https://c.tenor.com/fYKFtYSPTA8AAAAd/cat-dance.gif",
        ]
        await self.send_art_embed(ctx, evidence)

    @slash_command(name="peepotalk")
    async def peepo_talk(self, ctx: discord.ApplicationContext):
        """An NPC is chatting away!"""
        await self.send_art_embed(
            ctx,
            [
                "https://cdn.discordapp.com/attachments/787711120026501152/1021097375588159658/peepo-talk-peepo_transparent.gif"
            ],
        )


def setup(bot):
    bot.add_cog(Art(bot))
