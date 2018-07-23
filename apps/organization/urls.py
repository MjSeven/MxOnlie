from django.urls import path, include, re_path

from .views import OrgView, AddUserAskView

app_name = "organization"

urlpatterns = [
    # 课程机构首页
    path('list/', OrgView.as_view(), name='org_list'),
    path(r'add_ask/', AddUserAskView.as_view(), name='add_ask'),
]
