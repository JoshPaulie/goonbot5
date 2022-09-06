import random

import discord
from discord.commands import user_command
from discord.ext import commands
from goonbot import GoonBot
from pymongo.errors import DuplicateKeyError

# Current Tokens
COINS = "coins"
MILES = "miles"


class Games(commands.Cog, name="Games"):
    def __init__(self, bot: GoonBot):
        self.bot = bot

    async def get_tokens(self, user: discord.Member | discord.User):
        """Disgustingly hacky way to check how many of a specific token a user has.
        If user doesn't have any tokens, create a new document and give them 0 of token checked"""
        try:
            await self.bot.tokens.insert_one({"_id": user.id})
        except DuplicateKeyError:
            pass

        user_tokens = await self.bot.tokens.find_one({"_id": user.id})
        return user_tokens

    async def get_token_amount(self, token: str, user: discord.Member | discord.User):
        """Check to see how many of a specific token a user has"""
        user_tokens = await self.get_tokens(user)
        return user_tokens.get(token)

    async def change_token_amount(self, token: str, user: discord.Member | discord.User, change_amount: int):
        user_tokens = await self.get_tokens(user)
        await self.bot.tokens.update_one(user_tokens, {"$inc": {"coins": change_amount}})
        return user_tokens.get(token)

    @user_command(name="💰 Check Coins")
    async def check_coins_user_command(self, ctx: discord.ApplicationContext, member: discord.Member):
        """Check to see how many coin tokens a user has"""
        coin_amount = await self.get_token_amount(COINS, member)
        await ctx.respond(
            embed=discord.Embed(
                title=f"💰 {member.display_name} has {coin_amount} {'coin' if coin_amount == 1 else 'coins'}",
                color=discord.Color.blurple(),
            )
        )

    @user_command(name="👊 Mug")
    async def mug(self, ctx: discord.ApplicationContext, member: discord.Member):
        """Check to see how many coin tokens a user has"""
        """
        TODO
        [x] Make add token amount method
        [x] Cannot mug yourself
        [x] Check if victim has <0
        [] Actual game
        """
        if ctx.author == member:
            await ctx.respond(
                embed=discord.Embed(
                    title=f"In a failed attempt to mug themselves, {ctx.author.display_name} lost.",  # type: ignore
                    color=discord.Color.blurple(),
                ),
            )
            # return uncomment this to turn guard back on

        await self.change_token_amount(COINS, member, 0)
        coin_amount = await self.get_token_amount(COINS, member)
        if coin_amount < 1:
            await ctx.respond(
                embed=discord.Embed(
                    title=f"{member.display_name}'s wallet is empty",  # type: ignore
                    color=discord.Color.blurple(),
                ),
            )
            # return uncomment this to turn guard back on

        await ctx.respond(
            embed=discord.Embed(
                title=f"This isn't actually implemented yet. VSOON :))",
                color=discord.Color.blurple(),
            ),
            ephemeral=True,
        )


def setup(bot):
    bot.add_cog(Games(bot))
