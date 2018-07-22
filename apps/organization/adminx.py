import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'click_nums', 'address', 'city']
    list_filter = ['name', 'desc', 'click_nums', 'address', 'city', 'add_time']


class TeacherAdmin(object):
    list_display = ['name', 'org', 'work_company', 'fav_nums', 'add_time']
    search_fields = ['name', 'org', 'work_company', 'fav_nums']
    list_filter = ['name', 'org', 'work_company', 'fav_nums', 'add_time']

xadmin.site.register(CityDict, CityAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
