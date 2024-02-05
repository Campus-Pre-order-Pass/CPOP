from django.apps import AppConfig


class CustomerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Customer'
    verbose_name = "顧客"
    
    def ready(self):
        # Register checks
        import Customer.checks
        import Customer.signals  # 导入信号处理程序
        
