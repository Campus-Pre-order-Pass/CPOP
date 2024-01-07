# common_commands/management/commands/your_shared_command.py

from django.core.management.base import BaseCommand
from django.db.models import Count


class Command(BaseCommand):
    help = 'Your shared command description.'

    # def handle(self, *args, **options):
    #     # 获取不同 URL 的访问次数
    #     url_counts = RequestLog.objects.values('path').annotate(
    #         count=Count('path')).order_by('-count')

    #     for url_count in url_counts:
    #         print(f"URL: {url_count['path']}, Count: {url_count['count']}")
