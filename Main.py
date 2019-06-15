import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os
from discord import Game

bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
	print('Ready, Freddy')
    
@bot.command(name="mute")
@commands.has_permissions(kick_members=True, administrator=True)
async def _mute(ctx, user: discord.Member = None, *, arg = None):
	if user is None:
		await ctx.send("please provide a member")
		return False
	if arg is None:
		await ctx.send("please provide a reason to {}".format(user.name))
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
	await ctx.send(embed=embed)
	
@_mute.error
async def mute_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have requirement permission to use this command `kick_members`.".format(ctx.message.author.mention)
		await ctx.channel_send(ctx.message.channel, text)
	
@bot.command(name="unmute")
@commands.has_permissions(kick_members=True, administrator=True)
async def _unmute(ctx, user: discord.Member = None, *, arg = None):
	if user is None:
		await ctx.send("please provide a member")
		return False
	if arg is None:
		await ctx.send("please provide a reason to {}".format(user.name))
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
	await ctx.send(embed=embed)
	
@_unmute.error
async def unmute_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have requirement permission to use this command `kick_members`.".format(ctx.message.author.mention)
		await ctx.channel_send(ctx.message.channel, text)

@bot.command(name="kick")
@commands.has_permissions(kick_members=True)
async def _kick(ctx, user: discord.Member = None, *, arg = None):
	if user is None:
		await ctx.send("please provide a member")
		return False
	if arg is None:
		await ctx.send("please provide a reason to {}".format(user.name))
		return False
	if user.server_permissions.kick_members:
		return False
	reason = arg
	author = ctx.message.author
	await user.kick(arg=reason)
	embed = discord.Embed(title="Kick", description=" ", color=0x00ff00)
	embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
	embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
	embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
	await ctx.send(embed=embed)
	
@_kick.error
async def kick_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have requirement permission to use this command `kick_members`.".format(ctx.message.author.mention)
		await ctx.channel_send(ctx.message.channel, text)
  
@bot.command(name="ban")
@commands.has_permissions(ban_members=True)
async def _ban(ctx, user: discord.Member = None, *, arg = None):
	if user is None:
		await ctx.send("please provide a member")
		return False
	if arg is None:
		await ctx.send("please provide a reason to {}".format(user.name))
		return False
	if user.server_permissions.ban_members:
		return False
	reason = arg
	author = ctx.message.author
	await user.ban(arg=reason)
	embed = discord.Embed(title="Ban", description=" ", color=0xFF0000)
	embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
	embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
	embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
	await ctx.send(embed=embed)
	
@_ban.error
async def ban_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have requirement permission to use this command `ban_members`.".format(ctx.message.author.mention)
		await ctx.channel_send(ctx.message.channel, text)
		
@bot.command()
async def servers(ctx):
    for server in bot.servers:
        embed = discord.Embed(description="Server Name: {}, Server ID: {}".format(server.name, server.id))
        await ctx.send(embed=embed)

bot.run(os.environ['BOT_TOKEN'])
