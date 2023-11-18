from django.apps import AppConfig


class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Shop'
    verbose_name = "廠商"

    def ready(self):
        import Shop.signals  # 导入信号处理程序
