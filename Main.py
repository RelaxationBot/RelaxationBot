import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game

Client = discord.client
client = commands.Bot(command_prefix = '!')

@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, "Welcome to **Christian's Relaxation Server! Here you can listen to music, chat with friends, make new friends, and so much more!")
    print('Sent message to ' + member.name)

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='test'))
    print('Ready, Freddy')

@client.event
async def on_message(message):
    if message.content == '-relax':
        await client.send_message(message.channel, 'Sit back, take three deep breaths. In.......count to five....out....count to five. Do that ten times, lay back, and take a nap!')
    if message.content == '-asmr':
        await client.send_message(message.channel, 'https://www.youtube.com/channel/UClqNSqnWeOOUVkzcJFj4rBw')
    if message.content == '-help':
        await client.send_message(message.channel, '@ChristianBeneventi#0001 Contact him or another staff member!')
    if message.content == '-nou':
        await client.send_message(message.channel, '-yesu')
    if message.content == '-whoami':
        await client.send_message(message.channel, "A person. Are you dumb or somethin'?")
    if message.content == '-no':
        await client.send_message(message.channel,'yes')
    if message.content == '-yes':
        await client.send_message(message.channel,'no')
    if message.content == '-stop':
        await client.send_message(message.channel,'go')
    if message.content == '-ping':
        await client.send_message(message.channel,'pong')
    if message.content == '-die':
        await client.send_message(message.channel,'why')
    if message.content == '-commands':
        await client.send_message(message.channel,'```-commands, -relax, -asmr, -no, -yes, -nou, -help, -ping, -stop, -die, -troomp, -duck, -saloot, -hungry, -haylp, -ping, ')
    if message.content == '-troomp':
        em = discord.Embed(description='make merica grate egein')
        em.set_image(url='https://i.pinimg.com/736x/d6/3b/3e/d63b3e3087092152d34672504b4f3b7c.jpg')
        await client.send_message(message.channel, embed=em)
    await client.process_commands(message)

client.run(os.environ['BOT_TOKEN'])
