import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Welcome to **Christian's Relaxation Server!" Here you can listen to music, chat with friends, make new friends, and so much more!')
    print('Sent message to ' + member.name)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name='test'))
    print('Ready, Freddy')
