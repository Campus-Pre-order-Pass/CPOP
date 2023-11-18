# myapp/urls.py
from django.urls import path
from . import views

app_name = 'Track'  # 设置app_name

urlpatterns = [
    path('init', views.init, name='init'),

    # users
    path('user/<str:shop_id>',
         views.daily_new_users, name='user'),



    # merchant
    path('merchant/<str:uid>',
         views.merchant, name='merchant'),

    # test
    path('test/', views.test, name='test'),

]
