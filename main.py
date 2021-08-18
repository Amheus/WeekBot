
from asyncio import sleep
import configparser
from datetime import datetime
import discord
from discord.ext import commands, tasks
from discord.ext.commands import DefaultHelpCommand
from discord_slash import SlashCommand
import sys

from cogs.commands import Commands
from cogs.loops import activity_loop

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

    bot.loop.create_task(activity_loop(bot))


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
