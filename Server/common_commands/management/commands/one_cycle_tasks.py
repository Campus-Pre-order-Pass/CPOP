from django.core.management.base import BaseCommand

from MenuItem.tasks import create_daily_menu_status_models

from Shop.tasks import creat_shop_daily_instance


class Command(BaseCommand):
    help = 'Your shared command description.'

    def handle(self, *args, **options):
        shop_instance_result = creat_shop_daily_instance()
        menu_status_result = create_daily_menu_status_models()

        # 输出结果
        self.stdout.write(self.style.SUCCESS(
            f'Shop instance result: {shop_instance_result}'))
        self.stdout.write(self.style.SUCCESS(
            f'Menu status result: {menu_status_result}'))
