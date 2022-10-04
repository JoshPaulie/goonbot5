import random

import discord
from discord.commands import slash_command, user_command
from discord.ext import commands
from goonbot import GoonBot

COINS = "coins"


class MuggingGame(commands.Cog, name="Games"):
    def __init__(self, bot: GoonBot):
        self.bot = bot

    @user_command(name="💰 Check Coins")
    async def check_coins_user_command(self, ctx: discord.ApplicationContext, member: discord.Member):
        """Check to see how many coin tokens a user has"""
        coin_amount = await self.bot.get_token_amount(COINS, member)
        await ctx.respond(
            embed=discord.Embed(
                title=f"💰 {member.name} has {coin_amount} {'coin' if coin_amount == 1 else 'coins'}",
                color=discord.Color.blurple(),
            )
        )

    @slash_command()
    async def coins(self, ctx: discord.ApplicationContext):
        """Check how many coins everyone has 😏"""
        coins_embed = discord.Embed(title="Coins! 💰", color=discord.Color.blurple())

        # ? "Couldn't this be a list comprehension" ?
        # Nope. 😊
        token_docs = []
        token_docs_cursor = self.bot.tokens.find()
        async for doc in token_docs_cursor:
            token_docs.append(doc)

        #                LOL                #
        # ~~ future employers look away ~~  #
        coins_embed.description = "\n".join(
            [f"{ctx.guild.get_member(d['_id']).mention}: {d['coins']}" for d in token_docs]  # type: ignore
        )
        await ctx.respond(embed=coins_embed)

    @user_command(name="👊 Mug")
    @commands.cooldown(1, 60, type=commands.BucketType.user)
    async def mug(self, ctx: discord.ApplicationContext, member: discord.Member):
        """Mug someone for a chance to steal their coins!"""
        attacker = ctx.author
        victim = member

        # Embed that's to be built on during encounter
        mugging_embed = discord.Embed(color=discord.Color.blurple())

        # Get how many coins are in each wallet before encounter
        # The "end amount" will be manipulated throughout the encounter, eliminating the need for another server call later
        attacker_coin_amount_start = attacker_coin_amount_end = await self.bot.get_token_amount(COINS, attacker)  # type: ignore
        victim_coin_amount_start = victim_coin_amount_end = await self.bot.get_token_amount(COINS, victim)

        # Pick the amount lost if respective party were to lose an encounter
        # It is possible to lose upto 1/4 of one's current wallet in an encounter
        # If the user has <8 coins, only 1 coin can be taken at a time.
        attacker_mugging_amount = random.randint(1, attacker_coin_amount_start // 4 or 1)
        victim_mugging_amount = random.randint(1, victim_coin_amount_start // 4 or 1)

        # "You can't mug yourself" guard
        if attacker == victim:
            mugging_embed.title = f"In a failed attempt to mug themselves, {attacker.name} lost."  # type: ignore
            await ctx.respond(embed=mugging_embed)
            return

        """
        The actually mugging encounter is handled as follows
        - A random number is rolled, 1-3. This is stored in `mugging_outcome`
        - If 1: the attacker successfully mugs the victim and takes coins (if any)
        - If 2: the attacker was unsuccessful and no coins are changed.
        - If 3: the attacker was "VERY" unsuccessful, and will actually lose coins to the victim
        """
        mugging_outcome = random.randint(1, 3)
        match mugging_outcome:
            case 1:  # Mugging was successful
                mugging_embed.color = discord.Color.brand_green()
                mugging_embed.title = f"{attacker.name} mugged {victim.name}!"  # type: ignore
                if victim_coin_amount_start <= 0:  # If victim has no coins to be mugged
                    mugging_embed.description = f"But their wallet was empty!"
                else:
                    await self.bot.change_token_amount(COINS, victim, -victim_mugging_amount)
                    await self.bot.change_token_amount(COINS, attacker, victim_mugging_amount)  # type: ignore
                    victim_coin_amount_end -= victim_mugging_amount
                    attacker_coin_amount_end += victim_mugging_amount
                    mugging_embed.description = f"And got away with {victim_mugging_amount} {'coin' if victim_mugging_amount == 1 else 'coins'}!"

            case 2:  # Mugging was unsuccessful
                mugging_embed.title = f"{attacker.name} attempted to mug {victim.name}"  # type: ignore
                mugging_embed.description = "but they got away."
                mugging_embed.color = discord.Color.greyple()

            case 3:  # Mugging was VERY unsuccessful
                mugging_embed.title = f"{attacker.name} attempted to mug {victim.name}"  # type: ignore
                mugging_embed.color = discord.Color.dark_red()
                if attacker_coin_amount_start <= 0:  # Attacker lost to victim, but has no coins
                    mugging_embed.description = f"{victim.name} overcame {attacker.name}, but their wallet was empty."  # type: ignore
                else:
                    await self.bot.change_token_amount(COINS, victim, attacker_mugging_amount)
                    await self.bot.change_token_amount(COINS, attacker, -attacker_mugging_amount)  # type: ignore
                    victim_coin_amount_end += attacker_mugging_amount
                    attacker_coin_amount_end -= attacker_mugging_amount
                    mugging_embed.description = f"{victim.name} fought back, {attacker.name} lost {attacker_mugging_amount} {'coin' if attacker_mugging_amount == 1 else 'coins'}."  # type: ignore

        mugging_embed.add_field(name=f"{attacker.name}", value=f"{attacker.mention}\n💰 {str(attacker_coin_amount_end)}")  # type: ignore
        mugging_embed.add_field(
            name=f"{victim.name}", value=f"{victim.mention}\n💰 {str(victim_coin_amount_end)}"
        )
        await ctx.respond(embed=mugging_embed)

    @mug.error
    async def on_application_command_error(
        self, ctx: discord.ApplicationContext, error: discord.DiscordException
    ):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.respond(
                embed=discord.Embed(
                    title="You're on cooldown! 🥶",
                    description=f"You have **{round(ctx.command.get_cooldown_retry_after(ctx=ctx))}**s remaining",
                    color=discord.Color.from_rgb(78, 167, 232),
                ),
                ephemeral=True,
            )
        else:
            raise error  # Here we raise other errors to ensure they aren't ignored


def setup(bot):
    bot.add_cog(MuggingGame(bot))
