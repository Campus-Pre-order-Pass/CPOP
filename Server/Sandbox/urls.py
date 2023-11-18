from django.urls import path, include
from . import views

app_name = 'Sandbox'


urlpatterns = [
    # 獲取餐廳
    path('s',
         views.get_shop, name='shop'),
    path('s/<int:id>',
         views.get_shop, name='shop'),

    # 獲取餐廳 現在狀態
    path('s/<int:id>/current',
         views.ger_shop_current, name='current'),

    path('auth/<str:uid>',
         views.Auth.as_view(), name='current')
]
