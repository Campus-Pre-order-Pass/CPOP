# runapscheduler.py
import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util
from Printer.main import OrderInvoiceGenerator

# helper
from helper.task.current_state import update_current_state_action


class Command(BaseCommand):
    # ./manage.py order
    help = "Test the printer functionality"

    def handle(self, *args, **options):
        # Your logic for testing the printer goes here
        order_details_example = [
            ["哈哈: ", "11-05 10:30", ""],
            ["平台: ", "888", ""],
            ["總金額: ", "1000", ""],
            ["波士頓龍蝦蛋餅", "1", ""],
            ["雙色吐司", "1", "巧克力/奶酥"],
            ["紅茶", "1", "去冰"]
        ]

        # Assuming OrderInvoiceGenerator is in your_module
        invoice_generator = OrderInvoiceGenerator(IP="10.0.0.11")
        result = invoice_generator.generate_invoice(
            shop="B", order_details=order_details_example, print_invoice=True, show_invoice=False)

        # Output the result to the console
        if result:
            self.stdout.write(self.style.SUCCESS('Printer test successful'))
        else:
            self.stdout.write(self.style.ERROR('Printer test failed'))

        # You can also raise a CommandError if the test fails, which will stop further execution
        # Example:
        # if not result:
        #     raise CommandError('Printer test failed')
