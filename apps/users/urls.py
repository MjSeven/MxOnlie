from django.urls import path, re_path

from .views import UserInfoView


app_name = "users"

urlpatterns = [
    # 用户信息
    path('info/', UserInfoView.as_view(), name='user_info'),

]