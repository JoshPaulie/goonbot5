import random

import discord
from discord.commands import user_command
from discord.ext import commands
from goonbot import GoonBot
from pymongo.errors import DuplicateKeyError

# Current Tokens
COINS = "coins"
MILES = "miles"


class MuggingGame(commands.Cog, name="Games"):
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

    @commands.is_owner()
    @user_command(name="👊 Mug")
    async def mug(self, ctx: discord.ApplicationContext, member: discord.Member):
        """Check to see how many coin tokens a user has"""
        attacker = ctx.author
        victim = member

        if attacker == victim:
            await ctx.respond(
                embed=discord.Embed(
                    title=f"In a failed attempt to mug themselves, {attacker.display_name} lost.",  # type: ignore
                    color=discord.Color.blurple(),
                ),
            )
            return

        await self.change_token_amount(COINS, victim, 0)  # Makes sure "Coins are available in document"
        victim_coin_amount = await self.get_token_amount(COINS, victim)
        if victim_coin_amount < 1:
            await ctx.respond(
                embed=discord.Embed(
                    title=f"{victim.display_name}'s wallet is empty",  # type: ignore
                    color=discord.Color.blurple(),
                ),
            )
            return

        mugging_outcome = random.randint(1, 3)
        match mugging_outcome:
            case 1:
                # Mugging was successful
                await self.change_token_amount(COINS, victim, -1)
                await self.change_token_amount(COINS, attacker, 1)  # type: ignore
                await ctx.respond(
                    embed=discord.Embed(
                        title=f"{attacker.display_name} stole 1 coin from {victim.display_name}",  # type: ignore
                        color=discord.Color.brand_green(),
                    ),
                )
            case 2:
                # Mugging was unsuccessful
                await ctx.respond(
                    embed=discord.Embed(
                        title=f"{attacker.display_name} attempted to mug {victim.display_name}, but the got away.",  # type: ignore
                        color=discord.Color.greyple(),
                    ),
                )
            case 3:
                # Mugging was VERY unsuccessful
                # TODO make it so attacker with 0 coins can't go negative
                await self.change_token_amount(COINS, victim, 1)
                await self.change_token_amount(COINS, attacker, -1)  # type: ignore
                await ctx.respond(
                    embed=discord.Embed(
                        title=f"{victim.display_name} fought back, {attacker.display_name} lost a coin.",  # type: ignore
                        color=discord.Color.dark_red(),
                    ),
                )

    @mug.error
    async def on_application_command_error(
        self, ctx: discord.ApplicationContext, error: discord.DiscordException
    ):
        if isinstance(error, commands.NotOwner):
            await ctx.respond("Sorry, this is still under development! 🤓", ephemeral=True)
        else:
            raise error  # Here we raise other errors to ensure they aren't ignored


def setup(bot):
    bot.add_cog(MuggingGame(bot))
