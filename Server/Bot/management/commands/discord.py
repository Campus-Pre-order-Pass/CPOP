# yourapp/management/commands/linebot_commands.py
from django.core.management.base import BaseCommand
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi(
    'a9fG06auo1FlHgT2aiHaui8ctHfbDSrhBPrQihXeKvJz6DMwAxfLOBMWUm+31RID8Adw+W5XmnvQHNaD1UjTSckeuiV77kR2hw3tRGnSRtzusNtajG1Rjfr9ap8iyJqhTPjVIdmi3dZnez+nyu9/6wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('734ddec99f62171549a29f647c2edec5')


class Command(BaseCommand):
    help = 'Handle Line Bot events'

    def add_arguments(self, parser):
        pass  # You can add command-line arguments if needed

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Handling Line Bot events...'))

        # Implement your Line Bot event handling logic here
        # For example, you can set up a server to listen for Line Bot events

        # Example:
        # @handler.add(MessageEvent, message=TextMessage)
        # def handle_message(event):
        #     text = event.message.text
        #     reply_text = f"You said: {text}"
        #     line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_text))

        # Run your server or other necessary logic

        self.stdout.write(self.style.SUCCESS(
            'Line Bot event handling complete.'))
