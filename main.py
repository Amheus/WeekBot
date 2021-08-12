
import os
import discord
from discord.ext import commands, tasks
from discord.ext.commands import DefaultHelpCommand
from discord_slash import SlashCommand
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

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

    channel = bot.get_channel(int(os.getenv("CHANNEL_ID")))

    if channel is None:
        raise Exception("Please invite this bot into a server with a channel that you've specified in the `.env` file.")

    await channel.send(
        f'When it {current_day} https://www.youtube.com/watch?v={videos.get(current_day)}'
    )


@slash.slash(name='ping', description='Pings the bot, returns a response time.')
async def ping_test(ctx): ctx.send(f'response time: `{str(round(ctx.bot.latency * 1000))}`ms', hidden=True)


def main():
    bot.run(os.getenv("DISCORD_TOKEN"))


if __name__ == '__main__':
    if os.getenv("DISCORD_TOKEN") is None: raise Exception("Please provide a valid `DISCORD_TOKEN` in the `.env` file.")
    if not os.getenv("CHANNEL_ID").isdigit(): raise TypeError("Please provide a valid `CHANNEL_ID` in the `.env` file.")

    main()
