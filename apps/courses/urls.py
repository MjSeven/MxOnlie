from django.urls import path, re_path

from .views import CourseListView, CourseDetailView, CourseInfoView


app_name = "courses"

urlpatterns = [
    # 课程列表页
    path('list/', CourseListView.as_view(), name='course_list'),
    re_path(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),
    re_path(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view() ,name='course_info'),

]
