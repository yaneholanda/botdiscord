# Imports
import discord
from discord.ext import commands

# Credentials
TOKEN = 'OTE1NDIyODg3ODE1NTY1MzQz.YabYAA.UyyiiPcuOx08ZDDZ4B9kQfNZlK4'

# Create bot
client = commands.Bot(command_prefix='!')

# Startup Information
@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

# Command
@client.command()
async def helloworld(ctx):
    await ctx.send('Hello World!')
@client.command()    
async def amae(ctx):
    await ctx.send('TÁ CHATA')

client.run(TOKEN)