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
    print(name)
    title = ""
    for i in name:
        title += i + " "
    ytbe = gy.get_url1(title)
    embed = discord.Embed(
        title='Now playing:',
        description=ytbe[1],
        colour=discord.Colour.from_rgb(255, 0, 0)
    )
    await ctx.send(embed=embed)
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
        await ctx.send(f'{ctx.message.author.mention}, музыка уже проигрывается.')

    else:
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)

        URL = info['formats'][0]['url']

        vc.play(
            discord.FFmpegPCMAudio(executable="C:\\XD\\python\\bot\\ffmpeg\\ffmpeg.exe", source=URL,
                                   **FFMPEG_OPTIONS))
        gy.num.clear()

        while vc.is_playing():
            await sleep(5)
        if not vc.is_paused():
            await vc.disconnect()


@client.command(name="stop")
async def stop(ctx):
    await vc.disconnect()


@client.command(name="night")
async def gn(ctx, username):
    await ctx.send(username + " говорит: сладких снов!!!")


# test functions
@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == cg.POST_ID:
        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        member = utils.get(message.guild.members, id=payload.user_id)
        print(message.guild.members)
        print(member)
        print(payload.member)
        emoji = str(payload.emoji)
        role = utils.get(message.guild.roles, id=cg.ROLES[emoji])
        await payload.member.add_roles(role)
        await message.remove_reaction(payload.emoji, member)


@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == cg.POST_ID:
        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        member = utils.get(message.guild.members, id=payload.user_id)
        print(message.guild.members)
        print(member)
        print(payload.member)
        emoji = str(payload.emoji)
        role = utils.get(message.guild.roles, id=cg.ROLES[emoji])
        await payload.member.remove_roles(role)


client.run(TOKEN)
