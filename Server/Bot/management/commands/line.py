# views.py
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


#
from django.core.management.base import BaseCommand


line_bot_api = LineBotApi(
    'a9fG06auo1FlHgT2aiHaui8ctHfbDSrhBPrQihXeKvJz6DMwAxfLOBMWUm+31RID8Adw+W5XmnvQHNaD1UjTSckeuiV77kR2hw3tRGnSRtzusNtajG1Rjfr9ap8iyJqhTPjVIdmi3dZnez+nyu9/6wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('734ddec99f62171549a29f647c2edec5')


class Command(BaseCommand):
    help = 'Handle Line Bot events'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Handling Line Bot events...'))

        # Example of handling text messages
        text_message_event = MessageEvent(
            message=TextMessage(text='hello'),
            source=None  # You may need to create a proper source object
        )

        # Call the handle_message function directly
        handle_message(text_message_event)

        self.stdout.write(self.style.SUCCESS(
            'Line Bot event handling complete.'))


def handle_message(event):
    text = event.message.text
    reply_text = f"You said: {text}"
    line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text=reply_text))
