# runapscheduler.py
import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand

from Printer.main import OrderInvoiceGenerator

# helper
from helper.task.current_state import update_current_state_action


class Command(BaseCommand):
    # ./manage.py order
    help = "Test the printer functionality"

    def handle(self, *args, **options):
        # Your logic for testing the printer goes here
        order_details_example = [
            ["時間: ", "11-05 10:30", ""],
            ["平台: ", "123", ""],
            ["總金額: ", "85", ""],
            ["滷肉飯", "1", ""],
            ["綠豆牛奶冰沙", "1", ""]
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
