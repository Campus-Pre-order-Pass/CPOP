from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views import View
# rate
from django_ratelimit.decorators import ratelimit


def custom_ratelimit(rate, method="GET", key='ip'):
    """Create a custom rate limit"""
    def decorator(view_func):
        def wrapped_view(request, *args, **kwargs):
            # TODO: TESTING
            if settings.TEST:
                # 在测试环境中禁用装饰器
                return view_func(request, *args, **kwargs)
            return ratelimit(key=key, rate=rate, method=method)(view_func)(request, *args, **kwargs)

        return wrapped_view

    return decorator
