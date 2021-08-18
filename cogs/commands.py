
import discord
from discord.ext import commands
from discord_slash import cog_ext


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name='ping', description='Pings the bot, returns a response time.')
    async def ping_test(self, ctx):
        await ctx.send(f'response time: `{str(round(ctx.bot.latency * 1000))}`ms', hidden=True)

    @cog_ext.cog_slash(name='about', description='Returns information on the bot.')
    async def about(self, ctx):
        await ctx.send(
            embed=discord.Embed(
                title=f"WeekBot",
                description=f"""
    A bot that posts a video for that day once a day, every day.

    Created by `Joel Adams` (https://github.com/JoelLucaAdams).
    Further development by `Sam Lewis` (https://github.com/Amheus).
                """,
                colour=discord.Colour.blurple()
            ),
            hidden=True
        )
