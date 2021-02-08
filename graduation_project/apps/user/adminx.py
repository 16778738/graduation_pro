import xadmin
from user.models import Teacher, Student


# 将教师注册到后台
class TeacherAdmin(object):
    list_display = ('id', 'name', 'sex', 'dept', 'password', 'email', 'birth')  # 要显示哪些信息
    list_display_links = ('id', 'name')
    search_fields = ['name', 'dept', 'birth']
    list_filter = ['name', 'dept']


xadmin.site.register(Teacher, TeacherAdmin)


class StudentAdmin(object):
    list_display = ('id', 'name', 'sex', 'dept', 'major', 'password', 'email', 'birth')  # 要显示哪些信息
    list_display_links = ('id', 'name')  # 点击哪些信息可以进入编辑页面
    search_fields = ['name', 'dept', 'major', 'birth']  # 指定要搜索的字段，将会出现一个搜索框让管理员搜索关键词
    list_filter = ['name', 'dept', 'major', 'birth']  # 指定列表过滤器，右边将会出现一个快捷的过滤选项


xadmin.site.register(Student, StudentAdmin)
