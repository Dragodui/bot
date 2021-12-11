import config as cg
import discord
from discord.ext import commands
from dotenv import load_dotenv
from stata import get_url
from selenium.webdriver.chrome.options import Options
from asyncio import sleep
from youtube_dl import YoutubeDL
import get_yt as gy
from discord import utils

ytbe = ()
k = 0
options = Options()
options.headless = True
load_dotenv()
TOKEN = cg.TOKEN
GUILD = cg.GUILD_NAME
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='!')
YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'False'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
q = []


@client.event
async def on_ready():
    for guild in client.guilds:
        print(guild)
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


# wot stat
@client.command(name="stat")
async def show_stat(ctx, nickname):
    print(nickname)
    embed = discord.Embed(
        title='Статистика ' + nickname,
        description=get_url(options, nickname),
        colour=discord.Colour.from_rgb(255, 0, 0)
    )
    await ctx.send(embed=embed)


# music
@client.command(pass_context=True, name="play")
async def p1(ctx, *name):
    global ytbe
    title = ""
    for i in name:
        title += i + " "
    if k == 0:
        q.append(title)
    ytbe = gy.get_url1(title)
    print(ytbe)
    url = ytbe[0]
    await yt(ctx, url)


async def yt(ctx, url):
    global vc
    print(url)
    try:
        voice_channel = ctx.message.author.voice.channel
        vc = await voice_channel.connect()
    except:
        print('Уже подключен или не удалось подключиться')

    if vc.is_playing():
        pass

    else:
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)

        URL = info['formats'][0]['url']

        vc.play(
            discord.FFmpegPCMAudio(executable="C:\\XD\\python\\bot\\ffmpeg\\ffmpeg.exe", source=URL,
                                   **FFMPEG_OPTIONS))
        embed = discord.Embed(
            title='Now playing:',
            description=ytbe[1],
            colour=discord.Colour.from_rgb(255, 0, 0)
        )
        await ctx.send(embed=embed)
        q.remove(q[0])
        gy.num.clear()

        while vc.is_playing():
            await sleep(5)
        if not vc.is_paused():
            await vc.disconnect()


@client.command(name="stop")
async def stop(ctx):
    global k
    if len(q) == 0:
        await vc.disconnect()
        k = 0
    else:
        k += 1
        await vc.disconnect()
        await p1(ctx, q[0])


@client.command(name="pause")
async def pause(ctx):
    vc.pause()
    embed = discord.Embed(title="Pause", description="playing is paused", colour=discord.Colour.from_rgb(255, 0, 0))
    await ctx.send(embed=embed)


@client.command(name="resume")
async def resume(ctx):
    vc.resume()
    embed = discord.Embed(title="Pesume", description="playing is continue", colour=discord.Colour.from_rgb(255, 0, 0))
    await ctx.send(embed=embed)


@client.command(name="night")
async def gn(ctx, username):
    await ctx.send(username + " говорит: сладких снов!!!")


client.run(TOKEN)
