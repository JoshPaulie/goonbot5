import random

import discord
from discord.commands import user_command
from discord.ext import commands
from goonbot import GoonBot

COINS = "coins"


class MuggingGame(commands.Cog, name="Games"):
    def __init__(self, bot: GoonBot):
        self.bot = bot

    @user_command(name="💰 Check Coins")
    async def check_coins_user_command(self, ctx: discord.ApplicationContext, member: discord.Member):
        """Check to see how many coin tokens a user has"""
        await self.bot.change_token_amount(COINS, member, 0)  # Adds 'Coins' token to document if not already
        coin_amount = await self.bot.get_token_amount(COINS, member)
        await ctx.respond(
            embed=discord.Embed(
                title=f"💰 {member.display_name} has {coin_amount} {'coin' if coin_amount == 1 else 'coins'}",
                color=discord.Color.blurple(),
            )
        )

    @user_command(name="👊 Mug")
    @commands.cooldown(1, 60, type=commands.BucketType.user)
    async def mug(self, ctx: discord.ApplicationContext, member: discord.Member):
        """Mug someone for a chance to steal their coins!"""
        attacker = ctx.author
        victim = member

        attacker_coin_amount = await self.bot.get_token_amount(COINS, attacker)  # type: ignore
        victim_coin_amount = await self.bot.get_token_amount(COINS, victim)

        attacker_mugging_amount = random.randint(1, attacker_coin_amount // 4 or 1)
        victim_mugging_amount = random.randint(1, attacker_coin_amount // 4 or 1)

        if attacker == victim:
            await ctx.respond(
                embed=discord.Embed(
                    title=f"In a failed attempt to mug themselves, {attacker.display_name} lost.",  # type: ignore
                    color=discord.Color.blurple(),
                ),
            )
            return

        mugging_outcome = random.randint(1, 3)
        match mugging_outcome:
            case 1:
                # Mugging was successful
                if victim_coin_amount <= 0:
                    await ctx.respond(
                        embed=discord.Embed(
                            title=f"{attacker.display_name} mugged {victim.display_name}!",  # type: ignore
                            description=f"But their wallet was empty!",  # type: ignore
                            color=discord.Color.brand_green(),
                        ),
                    )
                    return

                await self.bot.change_token_amount(COINS, victim, -victim_mugging_amount)
                await self.bot.change_token_amount(COINS, attacker, victim_mugging_amount)  # type: ignore
                await ctx.respond(
                    embed=discord.Embed(
                        title=f"{attacker.display_name} mugged {victim.display_name}!",  # type: ignore
                        description=f"And got away with {victim_mugging_amount} {'coin' if victim_mugging_amount == 1 else 'coins'}!",  # type: ignore
                        color=discord.Color.brand_green(),
                    ),
                )
            case 2:
                # Mugging was unsuccessful
                await ctx.respond(
                    embed=discord.Embed(
                        title=f"{attacker.display_name} attempted to mug {victim.display_name}",  # type: ignore
                        description=f"but they got away.",  # type: ignore
                        color=discord.Color.greyple(),
                    ),
                )
            case 3:
                # Mugging was VERY unsuccessful
                if attacker_coin_amount <= 0:
                    await ctx.respond(
                        embed=discord.Embed(
                            title=f"{attacker.display_name} attempted to mug {victim.display_name}",  # type: ignore
                            description=f"{victim.display_name} overcame {attacker.display_name}, but their wallet was empty.",  # type: ignore
                            color=discord.Color.dark_red(),
                        ),
                    )
                    return

                await self.bot.change_token_amount(COINS, victim, attacker_mugging_amount)
                await self.bot.change_token_amount(COINS, attacker, -attacker_mugging_amount)  # type: ignore
                await ctx.respond(
                    embed=discord.Embed(
                        title=f"{attacker.display_name} made a grave mistake..",  # type: ignore
                        description=f"{victim.display_name} fought back, {attacker.display_name} lost {attacker_mugging_amount} {'coin' if attacker_mugging_amount == 1 else 'coins'}.",  # type: ignore
                        color=discord.Color.dark_red(),
                    ),
                )

    @mug.error
    async def on_application_command_error(
        self, ctx: discord.ApplicationContext, error: discord.DiscordException
    ):
        if isinstance(error, commands.NotOwner):
            await ctx.respond("Sorry, this is still under development! 🤓", ephemeral=True)
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.respond(
                discord.Embed(
                    title="You're on cooldown! 🥶",
                    description=f"{ctx.command.get_cooldown_retry_after}s remaining",
                ),
                ephemeral=True,
            )
        else:
            raise error  # Here we raise other errors to ensure they aren't ignored


def setup(bot):
    bot.add_cog(MuggingGame(bot))
