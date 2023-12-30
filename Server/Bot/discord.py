import discord
from discord.ext import commands

# 创建Bot实例
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')


@commands.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

# 运行Bot
bot.run('YOUR_DISCORD_BOT_TOKEN')
