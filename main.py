import discord
from discord.ext import commands
import random
from mp3 import *


bot = commands.Bot(command_prefix='!!')

@bot.event
async def on_ready():
    print('준비완료')



@bot.command()
async def 주사위(ctx):
    a = random.randrange(1,101)
    await ctx.send(a)


@bot.command()
async def p(ctx, *, k):
    a = VideosSearch(k, limit=1)
    link = a.resultComponents
    url = link[0]['link']
    channel = ctx.author.voice.channel
    if bot.voice_clients == []:
        await channel.connect()
        await ctx.send("빠끄~")

    ydl_opts = {'format': 'bestaudio'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
    voice = bot.voice_clients[0]
    voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))

@bot.command()
async def stop(ctx):
    if bot.voice_clients[0].is_playing():
        bot.voice_clients[0].stop()

@bot.command()
async def leave(ctx):
    await bot.voice_clients[0].disconnect()





bot.run('OTE0MTQ4OTM1NjEyOTAzNDI0.YaI1ig.Th2GwGYycO4hntbvkGf_ohs3IhI')