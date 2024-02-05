from django.conf import settings

from functools import wraps
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from django.http import HttpResponseForbidden 

def base_protection_decorators_v0(view_func):
    if settings.DEBUG:
        # 如果處於 DEBUG 模式，不應用 CSRF 保護和登錄裝飾器
        return view_func

    # 否則，應用 CSRF 保護和登錄裝飾器
    
    # method_decorator(login_required, name='dispatch')先不用
    decorated_view = method_decorator(csrf_protect, name='dispatch')(
        method_decorator(ensure_csrf_cookie, name='dispatch')(
            (view_func)
        )
    )
    return decorated_view


def user_passes_test_404(test_func):
    """confirm user groups

    Args:
        test_func (_type_): _description_
    """
    def decorator(view_func):
        def wrapped(request, *args, **kwargs):
            if not test_func(request):
                raise HttpResponseForbidden("HttpResponseForbidden")
            return view_func(request, *args, **kwargs)
        return wrapped
    return decorator



# # 使用 apply_decorators 裝飾你的函數視圖
# @apply_decorators
# def your_function_based_view(request):
#     # 這裡放置你的函數視圖邏輯
#     pass


def firebase_login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # 檢查是否有 Firebase 相關信息
        if hasattr(request.user, 'firebase_auth'):
            # 在這裡處理已通過 Firebase 身份驗證的用戶邏輯
            return view_func(request, *args, **kwargs)
        else:
            # 如果未通過 Firebase 身份驗證，返回 HTTP 403 Forbidden
            return HttpResponseForbidden("You do not have permission to access this resource.")
    
    return _wrapped_view