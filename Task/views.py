# django
import logging
from django.shortcuts import render
from django.conf import settings

# rest
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# job
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

# limit
from django.shortcuts import render
from django_ratelimit.decorators import ratelimit

# helper
from helper.task.current_state import update_current_state_action

# ----------------------------------------------------------------


# base task
scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'default')


@api_view(['POST'])
@ratelimit(key=settings.RATELIMIT_KEY, rate=settings.RATELIMITS_ADMIN)
def update_current_state(request):
    cron_trigger = CronTrigger(hour=0, minute=0)

    # 添加定时任务
    scheduler.add_job(update_current_state_action,
                      trigger=cron_trigger, id="update_current_state")


@ratelimit(key=settings.RATELIMIT_KEY, rate=settings.RATELIMITS_ADMIN)
@api_view(["DELETE"])
def stop_all_tasks(request):
    scheduler.remove_all_jobs()
    # Library.objects.all().delete()

    return Response({"status": "success"})


def test(request):
    logger = logging.getLogger('LoggerName')
    logger.info('The info message')
    logger.warning('The warning message')
    logger.error('The error message')


# job =================================================================
register_events(scheduler)
scheduler.start()
