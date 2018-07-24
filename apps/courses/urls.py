from django.urls import path, re_path

from .views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddCommetsView
from .views import VideoPlayView


app_name = "courses"

urlpatterns = [
    # 课程列表页
    path('list/', CourseListView.as_view(), name='course_list'),
    # 课程详情
    re_path(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),
    # 课程章节信息
    re_path(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view() ,name='course_info'),
    # 课程评论
    re_path(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view() ,name='course_comment'),
    # 添加课程评论
    path('add_comment/', AddCommetsView.as_view(), name='add_comments'),
    # 视频地址
    re_path(r'^video/(?P<video_id>\d+)/$', VideoPlayView.as_view(), name='video_play'),

]
