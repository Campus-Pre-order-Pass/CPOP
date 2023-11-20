# django
import logging
from django.shortcuts import render
from django.conf import settings

# rest
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# limit
from django.shortcuts import render
from django_ratelimit.decorators import ratelimit

# helper
from helper.task.current_state import update_current_state_action

# q
from django_q.tasks import schedule


def runs_base_task():
    update_current_state_action()


# Schedule the task to run every day at midnight
schedule('Task.tasks.runs_base_task', '0 0 * * *')
