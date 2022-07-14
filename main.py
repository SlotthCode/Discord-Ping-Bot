
from tokenize import Name
import discord, time
from discord.ext import commands
from discord.utils import get
import asyncio
from config import token
from config import pingrole
from config import channel1
from config import channel2
from config import channel3
from config import channel4
from config import channel5
from config import channel6
from config import channel7
from config import channel8
from config import channel9
from config import channel10



bot = commands.Bot(command_prefix="!")
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Ping Bot made by Slotth"))
    print("Bot is now online!")
    
@bot.event
async def on_command_error(ctx, error):
    await ctx.reply("Not a command, try see !help")


@bot.command()
async def pingpeople(ctx):
    channel = bot.get_channel(channel1)
    channel2 = bot.get_channel(channel2)
    channel3 = bot.get_channel(channel3)
    channel4 = bot.get_channel(channel4)
    channel5 = bot.get_channel(channel5)
    channel6 = bot.get_channel(channel6)
    channel7 = bot.get_channel(channel7)
    channel8 = bot.get_channel(channel8)
    channel9 = bot.get_channel(channel9)
    channel10 = bot.get_channel(channel10)
    ping = discord.utils.get(ctx.guild.roles, id=pingrole)
    while True:
        await channel.send(f"{ping.mention}")
        await asyncio.sleep(0.3)
        await channel2.send(f"{ping.mention}")
        await asyncio.sleep(0.3)
        await channel3.send(f"{ping.mention}")
        await asyncio.sleep(0.3)
        await channel4.send(f"{ping.mention}")
        await asyncio.sleep(0.3)
        await channel5.send(f"{ping.mention}")
        await asyncio.sleep(0.3)
        await channel6.send(f"{ping.mention}")
        await asyncio.sleep(0.3)
        await channel7.send(f"{ping.mention}")
        await asyncio.sleep(0.3)
        await channel8.send(f"{ping.mention}")
        await asyncio.sleep(0.3)
        await channel9.send(f"{ping.mention}")
        await asyncio.sleep(0.3)
        await channel10.send(f"{ping.mention}")
        await asyncio.sleep(15)

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))
@bot.command()
async def help(ctx):
    await ctx.send("Help, Ping, Pingpeople")


bot.run(token)