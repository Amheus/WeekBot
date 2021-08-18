import configparser
from datetime import datetime

import discord
from discord.ext import tasks


@tasks.loop(hours=24)
async def activity_loop(bot):
    await bot.wait_until_ready()
    if bot.is_closed(): return

    current_day = datetime.today().strftime("%A")

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
            raise Exception(
                "Please invite this bot into a server with a channel that you've specified in the `.env` file."
            )

        await channel.send(
            f'When it {current_day} {config.get("videos", current_day.lower())}'
        )
