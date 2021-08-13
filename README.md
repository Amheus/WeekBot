# __**WeekBot**__

<h1 id="1. Contents">1. Contents</h1>
<a href="#1. Contents">1. Contents</a><br>
<a href="#2. About">2. About</a><br>
<a href="#3. Requirements">3. Requirements</a><br>
<a href="#3.1. Packages">3.1. Packages</a><br>
<a href="#3.2. .env File">3.2. .env File</a><br>
<a href="#3.2.1. DISCORD_TOKEN">3.2.1 `DISCORD_TOKEN`</a><br>
<a href="#3.2.2. CHANNEL_ID">3.2.2 `CHANNEL_ID`</a><br>
<a href="#4. Examples">4. Examples</a>

<h1 id="2. About">2. About</h1>
A Discord Bot that sends a message daily with a video for that day to a provided channel.


<h1 id="3. Requirements">3. Requirements</h1>
<h2 id="3.1. Packages">3.1. Packages</h2>
This bot requires the packages which are listed below:
- pip3 install discord
- pip3 install discord.py
- pip3 install discord-py-slash-command
- pip3 install python-dotenv

However, to make it easier for you, you can just run the following command:

`pip3 install -r requirements`

This will automatically download and install the packages listed in the `requirements` file.


<h2 id="3.2. .env File">3.2. `.env` File</h2>
This bot relies on a `.env` file being present, a template can be seen below, **both variables are required**.

```
DISCORD_TOKEN=""
CHANNEL_ID=
```

<h3 id="3.2.1. DISCORD_TOKEN">3.2.1. `DISCORD_TOKEN`</h3>
This is provided by Discord and can be obtained by:
1. Going to https://discord.com/developers/applications`.
2. Clicking on the bot.  If you have not yet created a bot, then click `New Application` in the top right.
3. Navigate to the `Bot` menu on the left-hand side.
4. Click `Copy` under `Click to Reveal Token` and paste into the `.env` file.  If you haven't created a bot, then press `Add Bot`, then `Yes, do it!`.

<h3 id="3.2.2. CHANNEL_ID">3.2.2. `CHANNEL_ID`</h2>
This is the ID of the channel you want WeekBot to send messages in.


<h1 id="4. Examples">4. Examples</h1>

![Preview](https://raw.githubusercontent.com/JoelLucaAdams/Weekbot/master/Preview.png)
