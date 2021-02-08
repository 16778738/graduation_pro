import xadmin
from record.models import Grade


class GradeAdmin(object):
    list_display = ('sid', 'subject', 'grade',)
    list_display_links = ('sid', 'subject', 'grade',)


xadmin.site.register(Grade, GradeAdmin)
