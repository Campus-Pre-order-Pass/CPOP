from functools import wraps
from django.db.models import Model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer  # 导入渲染器类

# 自定义通用异常处理装饰器


def handle_exceptions(model):
    """
    * 可以減少 tyr catch  寫法
    * 把 model 404 500 與 id 找不到給過濾掉
    """
    def decorator(view_class):
        class WrappedView(view_class):
            @wraps(view_class.__init__)
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def dispatch(self, request, *args, **kwargs):
                try:
                    return super().dispatch(request, *args, **kwargs)
                except model.DoesNotExist:
                    response = Response(
                        {'error': f'{model.__name__} not found'}, status=status.HTTP_404_NOT_FOUND)
                    response.accepted_renderer = JSONRenderer()
                    response.accepted_media_type = JSONRenderer.media_type
                    response.renderer_context = {}
                    return response
                except Exception as e:
                    """未知錯誤"""
                    response = Response(
                        {'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                    response.accepted_renderer = JSONRenderer()
                    response.accepted_media_type = JSONRenderer.media_type
                    response.renderer_context = {}
                    return response

        return WrappedView

    return decorator
