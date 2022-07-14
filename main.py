from tokenize import Name
import discord, time
from discord.ext import commands
from discord.utils import get
import asyncio
#made by slotth

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
    #Don't use "" in the channel do this ex. (937545678980)
    channel = bot.get_channel(channel id here)
    channel2 = bot.get_channel(channel id here)
    channel3 = bot.get_channel(channel id here)
    channel4 = bot.get_channel(channel id here)
    channel5 = bot.get_channel(channel id here)
    channel6 = bot.get_channel(channel id here)
    channel7 = bot.get_channel(channel id here)
    channel8 = bot.get_channel(Channel id here)
    channel9 = bot.get_channel(channel id here)
    channel10 = bot.get_channel(channel id here)
    #dont use "" do this ex. id=192038121
    ping = discord.utils.get(ctx.guild.roles, id=role ping id here)
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


bot.run("token here")
