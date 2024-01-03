"""
URL configuration for journeyechoes_server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import FileResponse
from django.conf import settings
import os
from django.conf.urls.static import static
from CSP.views import handle_csp_report

from helper.file import upload_vendor_image
import debug_toolbar   # 必要的导入

#
from rest_framework import permissions
# drf_yasg
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# 版本
V = settings.V


def serve_robots_txt(request):
    robots_txt_path = os.path.join(settings.BASE_DIR, 'robots.txt')
    return FileResponse(open(robots_txt_path, 'rb'))


def trigger_error(request):
    division_by_zero = 1 / 0


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [


    # TODO: default url is admin site
    path('admin/', admin.site.urls),


    # log
    path('logs/', include('log_viewer.urls')),

    # snadbax
    # path('v0/sandbox/api/', include('Sandbox.urls', namespace='Sandbox')),


    # # auth
    # path('v0/api/auth/', include('Auth.urls', namespace='Auth')),

    # customer
    path(f'{V}/api/c/',
         include('Customer.urls', namespace='Customer')),

    # shop
    path(f'{V}/api/s/', include('Shop.urls', namespace='Shop')),

    # order
    path(f'{V}/api/o/', include('Order.urls', namespace='Order')),

    # menuItem
    path(f'{V}/api/m/', include('MenuItem.urls', namespace='MenuItem')),

    # camera
    path(f'{V}/api/camera/', include('Camera.urls', namespace='Camera')),


    # # file
    # path('vendor/<int:vendor_id>/upload_image/',
    #      upload_vendor_image, name='upload_vendor_image'),


    # debug
    path('sentry-debug/', trigger_error),

    # csp report
    path('csp-report-endpoint/', handle_csp_report, name='csp-report-endpoint'),

    # rest_framework
    path('api-auth/', include('rest_framework.urls')),


    # 添加 drf-yasg 自动生成的 API 文档 URL
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),

    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),



    # robots
    path('robots.txt', serve_robots_txt, name='robots_txt'),


]

# GET MEDIA_URL
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)),)
