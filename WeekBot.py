import os

import logging

import discord
from discord.ext import commands
from discord.ext.commands import DefaultHelpCommand
from dotenv import load_dotenv
from datetime import datetime, date
import asyncio

# logs data to the discord.log file, if this file doesn't exist at runtime it is created automatically
from cogs.utilities import Utilities

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)  # logging levels: NOTSET (all), DEBUG (bot interactions), INFO (bot connected etc)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


# load the private discord token from .env file.
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


# Initialise the Bot object with an accessible help Command object
helpCommand = DefaultHelpCommand()

bot = commands.Bot(
    command_prefix="!",
    help_command=helpCommand
)

# Setup the General cog with the help command
generalCog = Utilities()
bot.add_cog(generalCog)
helpCommand.cog = generalCog


@bot.event
async def on_ready():
    """
    Do something when the bot is ready to use.
    """
    print(f'{bot.user.name} has connected to Discord!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'it be {datetime.today().strftime("%A")}'))
    bot.loop.create_task(activity_loop())


async def activity_loop():
    """
    Cycles through different bot activities
    Sends a message each day with a respective YouTube link and then sleeps for 1 day
    """
    await bot.wait_until_ready()

    current_time = datetime.today()
    videos = ["https://www.youtube.com/watch?v=z8bItnmItq4", "https://www.youtube.com/watch?v=CY8a4uh_PdI", "https://www.youtube.com/watch?v=TGPQGRPAsGs", "https://www.youtube.com/watch?v=vZ-7GjIFLME", "https://www.youtube.com/watch?v=qFoEBIfVj9M", "https://www.youtube.com/watch?v=Dzt7OZ2SpOE", "https://www.youtube.com/watch?v=Zfjk5SeevLM"]
    ctx = bot.get_channel(813898417943871578)

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'it be {current_time.strftime("%A")}'))
    await ctx.send(f'When it {current_time.strftime("%A")} {videos[current_time.weekday()]}')

    await asyncio.sleep(86400)


@bot.event
async def on_command_error(ctx, error):
    """
    Handle the Error message in a nice way.
    """
    if hasattr(ctx.command, 'on_error'):
            return
    elif isinstance(error, commands.errors.CheckFailure):
        await ctx.send(error)
    elif isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send('You are missing a required argument.')
    elif isinstance(error, commands.errors.CommandNotFound):
        pass
    else:
        await ctx.send('You are missing a required argument.')
        logging.error(error)

# Start the bot
bot.run(TOKEN)
