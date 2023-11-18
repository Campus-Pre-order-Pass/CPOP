"""
URL configuration for Backend project.

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

from helper.file import upload_vendor_image


def serve_robots_txt(request):
    robots_txt_path = os.path.join(settings.BASE_DIR, 'robots.txt')
    return FileResponse(open(robots_txt_path, 'rb'))


urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # log
    path('logs/', include('log_viewer.urls')),

    # snadbax
    path('v0/sandbox/api/', include('Sandbox.urls', namespace='Sandbox')),


    # auth
    path('v0/api/auth/', include('Auth.urls', namespace='Auth')),


    # shop
    path('v0/api/s/', include('Shop.urls', namespace='Shop')),

    # menuItem
    path('v0/api/m/', include('MenuItem.urls', namespace='MenuItem')),


    # # file
    # path('vendor/<int:vendor_id>/upload_image/',
    #      upload_vendor_image, name='upload_vendor_image'),

    # robots
    path('robots.txt', serve_robots_txt, name='robots_txt'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
