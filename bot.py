#Here I am getting my personal bot going from offline to online

import discord
from discord.ext import commands
import responses


intents = discord.Intents.all()
intents.typing = False
intents.presences = False

TOKEN = INSERT TOKEN HERE'
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} is now running!')


client.run(TOKEN)






