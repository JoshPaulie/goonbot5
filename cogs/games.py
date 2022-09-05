import discord
from discord.commands import user_command
from discord.ext import commands
from goonbot import GoonBot


class Games(commands.Cog, name="Games"):
    def __init__(self, bot: GoonBot):
        self.bot = bot

    async def get_token_amount(self, token: str, user: discord.Member | discord.User):
        user_tokens = self.bot.tokens.find_one({"_id": user.id})
        return user_tokens[token]

    @user_command()
    async def get_borb_amount(self, ctx: discord.ApplicationContext, member: discord.Member):
        """testing"""
        borb_amount = await self.get_token_amount("borb", member)
        await ctx.respond(borb_amount)  # type: ignore


def setup(bot):
    bot.add_cog(Games(bot))
