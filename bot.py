import config as cg
import discord
import random
from discord.ext import commands
from discord.ext.commands import Greedy
from dotenv import load_dotenv

load_dotenv()
TOKEN = cg.TOKEN
GUILD = cg.GUILD_NAME
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='!')


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


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    answers = ["укрофашист", "хохлинка", "ясно хохол в чате"]
    if 'укра' in message.content:
        response = random.choice(answers)
        await message.channel.send(response)
    await client.process_commands(message)


@client.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@client.command(name='kick')
async def kick_members(ctx, targets: Greedy[Member] ):
    if not len(targets):
        await ctx.send("no targets")


client.run(TOKEN)
