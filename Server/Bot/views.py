from django.http import HttpResponse
import discord
from discord.ext import commands

# rest_framework
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def send_discord_message(request):
    # 替换为你的 Discord Bot Token
    bot_token = 'YOUR_DISCORD_BOT_TOKEN'

    # 替换为你的 Discord 服务器的频道 ID
    channel_id = 'YOUR_DISCORD_CHANNEL_ID'

    # 创建 Bot 实例
    bot = commands.Bot(command_prefix='!')

    # 异步函数用于发送消息
    async def send_message():
        await bot.wait_until_ready()
        channel = bot.get_channel(int(channel_id))
        await channel.send('Hello from Django!')

    # 启动 Bot
    bot.loop.create_task(send_message())
    bot.run(bot_token)

    return HttpResponse('Message sent to Discord!')
