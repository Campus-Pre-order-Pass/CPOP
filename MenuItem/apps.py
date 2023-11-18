from django.apps import AppConfig


class MenuitemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MenuItem'
    verbose_name = "菜單"

    def ready(self):
        import Shop.signals  # 导入信号处理程序
