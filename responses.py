#Since we got bot.py to work and now the bot is online, now I am naking the bot to respond to users in my private (in-progress) discord server

import discord
import getting discord bot online first.py
from discord.ext import commands

@client.command()
async def hello(ctx):
    await ctx.send("Hello I am a bot created by Izhan")

#only got this one response working, I am currently working on how to get more than one response working 
