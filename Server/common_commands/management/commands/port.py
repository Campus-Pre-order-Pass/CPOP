# common_commands/management/commands/your_shared_command.py

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Your shared command description.'

    def handle(self, *args, **options):
        # 共享命令的逻辑
        self.stdout.write(self.style.SUCCESS(
            'Shared command executed successfully!'))
