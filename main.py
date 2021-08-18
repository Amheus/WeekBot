
import configparser
from asyncio import sleep
from time import strftime

import discord
from discord.ext import commands, tasks
from discord.ext.commands import DefaultHelpCommand
from discord_slash import SlashCommand
from datetime import datetime

helpCommand = DefaultHelpCommand()

bot = commands.Bot(
    command_prefix="!",
    intents=discord.Intents.default()
)
slash = SlashCommand(bot, sync_commands=True)


@bot.event
async def on_ready():
    print(f'--------------------------------------------------------------------'
          f'\n|  as of {datetime.utcnow()} - {bot.user} is operational  |'
          f'\n--------------------------------------------------------------------')
    activity_loop.start()


@tasks.loop(hours=24)
async def activity_loop():
    await bot.wait_until_ready()
    if bot.is_closed(): return

    current_day = datetime.today().strftime("%A")

    videos = {
        'Monday': 'z8bItnmItq4',
        'Tuesday': 'CY8a4uh_PdI',
        'Wednesday': 'TGPQGRPAsGs',
        'Thursday': 'vZ-7GjIFLME',
        'Friday': 'qFoEBIfVj9M',
        'Saturday': 'Dzt7OZ2SpOE',
        'Sunday': 'Zfjk5SeevLM'
    }

    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f'it be {current_day}'
        )
    )

    with open("config.ini") as file:
        config = configparser.RawConfigParser(allow_no_value=True)
        config.read_string(file.read())

        channel = bot.get_channel(config.getint('parameters', 'channel-id'))

    if channel is None:
        raise Exception("Please invite this bot into a server with a channel that you've specified in the `.env` file.")

    await channel.send(
        f'When it {current_day} https://www.youtube.com/watch?v={videos.get(current_day)}'
    )


@slash.slash(name='ping', description='Pings the bot, returns a response time.')
async def ping_test(ctx): ctx.send(f'response time: `{str(round(ctx.bot.latency * 1000))}`ms', hidden=True)


@slash.slash(name='about', description='Returns information on the bot.')
async def about(ctx):
    ctx.send(
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


def main():
    with open("config.ini") as file:
        config = configparser.RawConfigParser(allow_no_value=True)
        config.read_string(file.read())

        bot.run(config.get('discord', 'token'))


if __name__ == '__main__':
    main()
