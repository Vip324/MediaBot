<center>

<p align="center"><img src="img/Bot1.jpg" width="300" height="300"></p>

# @MediaFinder_Bot

[![GitHub issues](https://img.shields.io/github/issues/Vip324/MediaBot)](https://github.com/Vip324/MediaBot/issues)
[![GitHub license](https://img.shields.io/github/license/Vip324/MediaBot)](https://github.com/Vip324/MediaBot/blob/master/LICENSE)
[![GitHub forks](https://img.shields.io/github/forks/Vip324/MediaBot)](https://github.com/Vip324/MediaBot/network)
[![GitHub stars](https://img.shields.io/github/stars/Vip324/MediaBot)](https://github.com/Vip324/MediaBot/stargazers)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Vip324/MediaBot)
![GitHub watchers](https://img.shields.io/github/watchers/Vip324/MediaBot?style=social)
</center>

## Table of contents

1. [Main features](#General-information)
    1. [General information](#General-information)
    1. [User authorization](#User-authorization)
    1. [User capabilities](#User-capabilities)
2. [Technology Stack and modules](#Technology-Stack-and-modules)
3. [Bot Registration](#Registration-bot)
4. [Start and debug](#Start-and-debug)

------------
## Basic possibilities

## General information

<div align="justify">

## Table of contents
> Chatbots are a kind of assistant that communicates with users via messages and has many specific functions. The chatbot can be used both for sending out information and for collecting it. Today, messengers are in high demand, this is due to changes in the field of mobile Internet: high speeds, low price and widespread use of smartphones. The progressiveness of messengers can be compared to the phenomenon of a decade ago-the explosion of social media. Already, 2 billion people use messaging apps, and according to forecasts, the number of users will increase to 2.48 billion by 2021.Chatbots are a kind of assistant that communicates with users via messages and has many specific functions. The chatbot can be used both for sending out information and for collecting it.

>Today messengers are in great demand, this is due to the change in the field of mobile Internet: high speeds, low price and widespread use of smartphones. The progressiveness of messengers can be compared to the phenomenon of a decade ago-the explosion of social media. Already, 2 billion people use messaging apps, and according to forecasts, the number of users will increase to 2.48 billion by 2021. 

<b>MediaFinder_Bot</b> — this is a bot that aims to make it easier to search and view videos in General. You don't need to search for movies or TV series on a bunch of links or the Internet. Everything is in one single bot, just imagine. Launch our bot, enter the name of the movie and get a link to the movie no extra actions and opening thousands of links or tabs

[🔼Table of contents](#Table of contents)


## Authorization of users


User authorization in the bot is implemented as follows: when adding a bot for the first time, the user must send it the /start command (this is standard and provided by Telegram). The next step, the user can optionally subscribe to the mailing list of released new products in the world of movies


[🔼Table of contents](#Table of contents)



## User capabilities


Search for media content and subscribe to the newsletter


[🔼Table of contents](#Table of contents)


## Technology stack and modules

1) [python3](https://www.python.org/ "python3") — a high-level programming language focused on improving developer productivity and code readability.

2) [aiogram](https://docs.aiogram.dev/en/latest/ "aiogram") — aiogram is a pretty simple and fully asynchronous framework for Telegram Bot API written in Python 3.7 with asyncio and aiohttp. It helps you to make your bots faster and simpler.

3) [SQLite3](https://docs.python.org/2/library/sqlite3.html "SQLite3") – this is a standalone, server-free transactional mechanism for the SQL database.

4) [BeautifulSoup](https://pypi.org/project/beautifulsoup4/ "BeautifulSoup") - BeautifulSoup is a Python library for parsing HTML and XML documents. It is often used for scrolling web pages. BeautifulSoup allows you to transform a complex HTML document into a complex tree of various Python objects. These can be tags, navigation, or comments.

[🔼Table of contents](#Table of contents)


## Registering a bot

Telegram uses a special bot to manage bots [@BotFather](https://telegram.me/BotFather "@BotFather"). To create a new bot, send the `/newbot ' command.

BotFather will prompt you to enter the name of the new bot and the username for the bot's account. The name is displayed in the dialog box with the bot, and the user name is used for links to it.



In the response message, you get a token that you need to manage the bot via the API. You don't have to write the token, but you can always get it again with the `/token`command.
If the token has become known to someone else besides you, you need to generate a new token with the `/revoke ' command.

The old token will stop working.

Find a new bot in the search


Don't add the bot to your contacts yet. As you can see, the description window is empty. Set the text that will be displayed in the window for adding the bot. To do this, send BotFather the `/setdescription`command.

The description is displayed in a window with the title "What can this bot do?". The description text is limited to 512 characters, and line feeds are allowed.

To change the bot description in the user information window, send the `/setabouttext ' command to BotFather.

The description text in this window is limited to 120 characters. The bot also shows that the text should not contain line feeds, but the text with them is normally accepted.

If the bot is already added to contacts, the description in the client is not updated immediately after the commands /setabouttext, /setdescription and /setuserpic. It helps you restart the client, or delete the conversation with the bot and add it again.

The most noticeable part of the description is the avatar. To change it, enter the BotFather `/setuserpic ' command.

After entering it, send BotFather an image that will become the bot's avatar. The avatar is used in two places : in the user's description and in the image in the contact list. Moreover, in contacts, the image is cropped in the form of a circle.

All features can be viewed using the `/help ' command.

** Note: token is the only identification key to the bot. Don't post it anywhere, otherwise other people will be able to control Your bot. The bot with this token was deleted at the time of posting the article.**

[🔼Table of contents](#Table of contents)

### Installing and configuring the bot:

1. Install all dependencies with `MediaBot/requirements.txt`.
2. Enable the proxy (since the api and the telegram bot itself are under sanctions in the Russian Federation), [RiseupVPN] was used when working on the project(https://riseup.net/vpn "RiseupVPN").
3. Launch the file app.py.
4. Open the telergam (messenger) and search for @MediaFinderBot and click start. 
</div>

# @MediaFinderBot
