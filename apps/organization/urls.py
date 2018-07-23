from django.urls import path, re_path

from .views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView
from .views import AddFavView

app_name = "organization"

urlpatterns = [
    # 课程机构首页
    path('list/', OrgView.as_view(), name='org_list'),
    path(r'add_ask/', AddUserAskView.as_view(), name='add_ask'),
    re_path(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home'),
    re_path(r'^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name='org_home'),
    re_path(r'^desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name='org_desc'),
    re_path(r'^org_teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name='org_teacher'),

    # 机构收藏
    path(r'^add_fav/', AddFavView.as_view(), name='add_fav'),

]
