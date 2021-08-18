
from asyncio import sleep
import configparser
from datetime import datetime
import discord
from discord.ext import commands, tasks
from discord.ext.commands import DefaultHelpCommand
from discord_slash import SlashCommand
import sys

from cogs.commands import Commands

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

    with open("config.ini") as file:
        config = configparser.RawConfigParser(allow_no_value=True)
        config.read_string(file.read())
        if config.has_option('parameters', 'time') is True:
            while f'{datetime.now().hour}:{datetime.now().minute}' != config.get('parameters', 'time'): await sleep(1)

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


def validate_config():
    with open("config.ini") as file:
        config = configparser.RawConfigParser(allow_no_value=True)
        config.read_string(file.read())

        sys.tracebacklimit = 0

        if not config.has_option('discord', 'token'):
            raise ValueError('A discord token is required in the `config.ini` file!')
        if not config.has_option('parameters', 'channel-id'):
            raise ValueError('A channel id is required in the `config.ini` file!')

        if not config.get('parameters', 'channel-id').isdigit():
            raise ValueError('The channel-id must be an integer!')

        if config.has_option('parameters', 'time'):
            if len(config.get('parameters', 'time')) != 5:
                raise ValueError('The time must be of format `HH:MM`!')

    sys.tracebacklimit = None


def main():
    validate_config()
    with open("config.ini") as file:
        config = configparser.RawConfigParser(allow_no_value=True)
        config.read_string(file.read())

        bot.add_cog(Commands(bot))
        bot.run(config.get('discord', 'token'))


if __name__ == '__main__':
    main()
