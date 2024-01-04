from django.core.checks import Error, register


@register()
def custom_check_app1(app_configs, **kwargs):
    errors = []

    # 示例检查：检查是否在某个应用程序中定义了特定的模型
    from Shop.models import Vendor
    if Vendor._meta.verbose_name:
        errors.append(
            Error(
                "MyModel 在 app1 中没有定义 verbose_name。",
                id="Shop.E001",
            )
        )

    return errors
