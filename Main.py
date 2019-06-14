import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os
from discord import Game

bot = commands.Bot(command_prefix = '-')

@bot.event
async def on_member_join(member):
	print('Recognised that a member called ' + member.name + ' joined')
	await bot.send_message(member, "Welcome to **Christian's Relaxation Server! Here you can listen to music, chat with friends, make new friends, and so much more!")
	print('Sent message to ' + member.name)

@bot.event
async def on_ready():
	await bot.change_presence(game=discord.Game(name="test"))
	print('Ready, Freddy')

@bot.event
async def on_message(message):
	if message.content == '-relax':
		await bot.send_message(message.channel, 'Sit back, take three deep breaths. In.......count to five....out....count to five. Do that ten times, lay back, and take a nap!')
	if message.content == '-asmr':
		await bot.send_message(message.channel, 'https://www.youtube.com/channel/UClqNSqnWeOOUVkzcJFj4rBw')
	if message.content == '-help':
		await bot.send_message(message.channel, '@ChristianBeneventi#0001 Contact him or another staff member!')
	if message.content == '-nou':
		await bot.send_message(message.channel, '-yesu')
	if message.content == '-whoami':
		await bot.send_message(message.channel, "A person. Are you dumb or somethin'?")
	if message.content == '-no':
		await bot.send_message(message.channel,'yes')
	if message.content == '-yes':
		await bot.send_message(message.channel,'no')
	if message.content == '-stop':
		await bot.send_message(message.channel,'go')
	if message.content == '-ping':
		await bot.send_message(message.channel,'pong')
	if message.content == '-die':
		await bot.send_message(message.channel,'why')
	if message.content == '-commands':
		await bot.send_message(message.channel,'```-commands, -relax, -asmr, -no, -yes, -nou, -help, -ping, -stop, -die, -troomp, -duck, -saloot, -hungry, -haylp, -ping, ')
	if message.content == '-troomp':
		em = discord.Embed(description='make merica grate egein')
		em.set_image(url='https://i.pinimg.com/736x/d6/3b/3e/d63b3e3087092152d34672504b4f3b7c.jpg')
		await bot.send_message(message.channel, embed=em)
	await bot.process_commands(message)
    
@bot.command(name="mute", pass_context=True)
@commands.has_permissions(kick_members=True, administrator=True)
async def _mute(ctx, user: discord.Member = None, *, arg = None):
	if user is None:
		await bot.say("please provide a member")
		return False
	if arg is None:
		await bot.say("please provide a reason to {}".format(user.name))
		return False
	if user.server_permissions.kick_members:
		return False
	reason = arg
	author = ctx.message.author
	role = discord.utils.get(ctx.message.server.roles, name="Muted")
	await bot.add_roles(user, role)
	embed = discord.Embed(title="Mute", description=" ", color=0xFFA500)
	embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
	embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
	embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
	await bot.say(embed=embed)
	
@_mute.error
async def mute_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have requirement permission to use this command `kick_members`.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)
	
@bot.command(name="unmute", pass_context=True)
@commands.has_permissions(kick_members=True, administrator=True)
async def _unmute(ctx, user: discord.Member = None, *, arg = None):
	if user is None:
		await bot.say("please provide a member")
		return False
	if arg is None:
		await bot.say("please provide a reason to {}".format(user.name))
		return False
	if user.server_permissions.kick_members:
		return False
	reason = arg
	author = ctx.message.author
	role = discord.utils.get(ctx.message.server.roles, name="Muted")
	await bot.remove_roles(user, role)
	embed = discord.Embed(title="Unmute", description=" ", color=0x00ff00)
	embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
	embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
	embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
	await bot.say(embed=embed)
	
@_unmute.error
async def unmute_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have requirement permission to use this command `kick_members`.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)

@bot.command(name="kick", pass_context=True)
@commands.has_permissions(kick_members=True)
async def _kick(ctx, user: discord.Member = None, *, arg = None):
	if user is None:
		await bot.say("please provide a member")
		return False
	if arg is None:
		await bot.say("please provide a reason to {}".format(user.name))
		return False
	if user.server_permissions.kick_members:
		return False
	reason = arg
	author = ctx.message.author
	await bot.kick(user)
	embed = discord.Embed(title="Kick", description=" ", color=0x00ff00)
	embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
	embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
	embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
	await bot.say(embed=embed)
	
@_kick.error
async def kick_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have requirement permission to use this command `kick_members`.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)
  
@bot.command(name="ban", pass_context=True)
@commands.has_permissions(ban_members=True)
async def _ban(ctx, user: discord.Member = None, *, arg = None):
	if user is None:
		await bot.say("please provide a member")
		return False
	if arg is None:
		await bot.say("please provide a reason to {}".format(user.name))
		return False
	if user.server_permissions.ban_members:
		return False
	reason = arg
	author = ctx.message.author
	await bot.ban(user)
	embed = discord.Embed(title="Ban", description=" ", color=0xFF0000)
	embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
	embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
	embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
	await bot.say(embed=embed)
	
@_ban.error
async def ban_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have requirement permission to use this command `ban_members`.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)
	
@bot.command(name="warn", pass_context=True)
@commands.has_permissions(kick_members=True)
async def _warn(ctx, user: discord.Member = None, *, arg = None):
	if user is None:
		await bot.say("please provide a member")
		return False
	if arg is None:
		await bot.say("please provide a reason to {}".format(user.name))
		return False
	if user.server_permissions.kick_members:
		return False
	reason = arg
	author = ctx.message.author
	server = ctx.message.server
	embed = discord.Embed(title="Warn", description=" ", color=0x00ff00)
	embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
	embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
	embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
	await bot.say(embed=embed)
	await bot.send_message(user, "You have been warned for: {}".format(reason))
	await bot.send_message(user, "from: {} server".format(server))
	
@_warn.error
async def warn_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have requirement permission to use this command `kick_members`.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)

bot.run(os.environ['BOT_TOKEN'])
