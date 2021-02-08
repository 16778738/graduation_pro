import xadmin
from question.models import Question, Paper


class QuestionAdmin(object):
    list_display = ('id', 'subject', 'title', 'optionA', 'optionB', 'optionC', 'optionD', 'answer', 'level', 'score')


xadmin.site.register(Question, QuestionAdmin)


class PaperAdmin(object):
    list_display = ('tid', 'major', 'subject', 'exam_time')
    list_display_links = ('major', 'subject', 'exam_time')


xadmin.site.register(Paper, PaperAdmin)
