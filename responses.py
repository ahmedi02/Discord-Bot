#Since we got bot.py to work and now the bot is online, now I am coming the bot to respond to users on my private (in-progress) discord server

import discord
import getting discord bot online first.py
from discord.ext import commands

@client.command()
async def hello(welcome, paynent):
    await welcome.send("Hello i am bot")

#only got this one response working, I am currently working on how to get more than one response working 
