import discord
from discord.ext import commands
from bot_logic import sampah_anorganik, sampah_organik

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def anorganik(ctx):
    await ctx.send('Ini salah satu sampah anorganik:')
    await ctx.send(sampah_anorganik())

# bikin sendiri untuk sampah organik
@bot.command()
async def organik(ctx):
    await ctx.send('Ini salah satu sampah anorganik:')
    await ctx.send(sampah_organik())

bot.run('TOKEN MU TARO DISINI CUY')
