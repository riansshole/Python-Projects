import discord
from discord.ext import commands
from discord.utils import get

token = 'ODQwMTgxNzU4MDI0MjIwNjgz.YJUePA.Jm1vJ8lKP4JQ3z9FRpt0xYUd-xA'
client = commands.Bot(command_prefix= '=')

@client.event
async def on_ready():
    print ('Bot is ready.')

client.run(token)