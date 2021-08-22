
from asyncio import sleep
import configparser
from datetime import datetime
import discord
from discord.ext import commands
from discord.ext.commands import DefaultHelpCommand
from discord_slash import SlashCommand

from cogs.commands import Commands
from cogs.loops import activity_loop
from helpers import validate_config

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
            while datetime.now().strftime('%H:%M') != config.get('parameters', 'time'):
                await sleep(1)

    bot.loop.create_task(activity_loop(bot))


def main():
    validate_config()
    with open("config.ini") as file:
        config = configparser.RawConfigParser(allow_no_value=True)
        config.read_string(file.read())

        bot.add_cog(Commands(bot))
        bot.run(config.get('discord', 'token'))


if __name__ == '__main__':
    main()
