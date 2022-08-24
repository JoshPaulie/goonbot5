import random

import discord
from discord.commands import SlashCommandGroup
from discord.ext import commands
from goonbot import GoonBot


class Art(commands.Cog):
    def __init__(self, bot: GoonBot):
        self.bot = bot

    art_group = SlashCommandGroup("art", "goon curated memes")

    @staticmethod
    async def send_art_embed(ctx: discord.ApplicationContext, image: str | list) -> None:
        art_embed = discord.Embed()

        if isinstance(image, str):
            art_embed.set_image(url=image)
        elif isinstance(image, list):
            image = random.choice(image)
            art_embed.set_image(url=image)

        art_embed.set_author(name=ctx.command.name)  # type: ignore
        art_embed.color = discord.Color.blurple()
        await ctx.respond(embed=art_embed)

    @art_group.command()
    async def bringe(self, ctx: discord.ApplicationContext):
        """Better Cringe. Duh."""
        image = "https://cdn.discordapp.com/attachments/531913512822243358/651997904751427624/Hudboy.png"
        await self.send_art_embed(ctx, image)

    @art_group.command()
    async def gamerword(self, ctx: discord.ApplicationContext):
        """Small child with heart of stone"""
        image = "https://cdn.discordapp.com/attachments/531913512822243358/651997280290734101/gamer.jpg"
        await self.send_art_embed(ctx, image)

    @art_group.command()
    async def pizza(self, ctx: discord.ApplicationContext):
        """finna get pizza pied"""
        image = "https://cdn.discordapp.com/attachments/177125557954281472/731242309446008893/image0.jpg"
        await self.send_art_embed(ctx, image)

    @art_group.command()
    async def clown(self, ctx: discord.ApplicationContext):
        """...he's the joker...baby..."""
        image = "https://cdn.discordapp.com/attachments/177125557954281472/651996397041877006/clown_2.0.jpg"
        await self.send_art_embed(ctx, image)

    @art_group.command()
    async def ygg(self, ctx: discord.ApplicationContext):
        """You good girl?"""
        image = (
            "https://cdn.discordapp.com/attachments/"
            "733685825379893339/756322976034586654/c00a411b-1fea-4593-b528-56cfc2dea9cf.png"
        )
        await self.send_art_embed(ctx, image)

    @art_group.command()
    async def frog(self, ctx: discord.ApplicationContext):
        """Fantasy Frog Fetish"""
        image = [
            "https://i.imgur.com/lqZM3sR.png",
            "https://cdn.discordapp.com/attachments/177125557954281472/814729226031726632/1614310329958.jpg",
            "https://media1.tenor.com/images/ba97a5584efb72bdfa4feeacc83ea2c2/tenor.gif",
            "https://media1.tenor.com/images/bfeaafa2ff74d740f1920174ce796ef3/tenor.gif",
        ]
        await self.send_art_embed(ctx, image)

    @art_group.command()
    async def joker(self, ctx):
        """Lex Fully Evolved"""
        image = (
            "https://cdn.discordapp.com/attachments/"
            "177125557954281472/754429776571138238/lex_true_form.jpg"
        )
        await self.send_art_embed(ctx, image)

    @art_group.command()
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
        ]
        await self.send_art_embed(ctx, evidence)

    # @art_group.command()
    # async def rool(self, ctx: discord.ApplicationContext):
    #     """G8r man!"""
    #     image = "https://media1.tenor.com/images/c071dcb215cc774f730c1630a5971fb4/tenor.gif?itemid=12340096"
    #     await self.send_art_embed(ctx, image)


def setup(bot):
    bot.add_cog(Art(bot))
