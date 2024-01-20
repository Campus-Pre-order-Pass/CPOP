import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

from helper.tool.function import PrinterTool

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend.settings_prod')


app = Celery(
    'Backend',
    broker='pyamqp://celery:password123@rabbitmq:5672/my_vhost'

)


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# beat_schedule

# Shop
app.conf.beat_schedule = {
    'execute-every-minute': {
        'task': 'Shop.tasks.test',
        'schedule': crontab(minute='*'),
    },
    'execute-daily-menu-status-models-shop': {
        'task': 'Shop.tasks.creat_shop_daily_instance',
        'schedule': crontab(minute=0, hour=0),
    },
    'execute-daily-menu-status-models-menuitem': {
        'task': 'MenuItem.tasks.create_daily_menu_status_models',
        'schedule': crontab(minute=0, hour=0),
    },
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
