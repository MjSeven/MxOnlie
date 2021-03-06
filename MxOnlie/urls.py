"""MxOnlie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve

import xadmin

from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView
from users.views import ResetPwdView, ModifyPwdView, LogoutView, IndexView
from MxOnlie.settings import MEDIA_ROOT


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name="login"),
    path(r'logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name="register"),
    path('captcha/', include('captcha.urls')),
    path('active/<str:active_code>/', ActiveUserView.as_view(), name='user_active'),
    path('forget/', ForgetPwdView.as_view(), name= "forget_pwd"),
    path('reset/<str:active_code>/', ResetPwdView.as_view(), name="reset_pwd"),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),

    # 课程机构 url 配置
    path('org/', include('organization.urls', namespace='org')),

    # 课程相关 url 配置
    path('course/', include('courses.urls', namespace='course')),

    # 用户相关 url 配置
    path('users/', include('users.urls', namespace='users')),

    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT })

]

# 全局 404 500 页面配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'

# 在生产环境下时， DEBUG = False
# static 静态文件需要由 nginx 等代理
# 或者自己配 url static_root
