from django.conf import settings

# rate
from django_ratelimit.decorators import ratelimit


def custom_ratelimit(rate, method="GET", key='ip'):
    """Create a custom rate limit"""
    def decorator(view_func):
        def wrapped_view(request, *args, **kwargs):
            # TODO: 需要修改
            if settings.TEST:
                # 在测试环境中禁用装饰器
                return view_func(request, *args, **kwargs)
            return ratelimit(key=key, rate=rate, method=method)(view_func)(request, *args, **kwargs)

        return wrapped_view

    return decorator
