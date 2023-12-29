from celery import shared_task, signals
from django.core.mail import send_mail


@shared_task(ignore_result=True)
def test():
    print("ok")
