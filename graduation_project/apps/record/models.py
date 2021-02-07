from django.db import models
from home.baseModel import BaseModel

# Create your models here.
from user.models import Student


class Grade(BaseModel):
    sid = models.ForeignKey(Student, on_delete=models.CASCADE, default='')  # 添加外键
    subject = models.CharField('科目', max_length=20, default='')
    grade = models.IntegerField()

    def __str__(self):
        return '<%s:%s>' % (self.sid, self.grade);

    class Meta:
        db_table = 'grade'
        verbose_name = '成绩'
        verbose_name_plural = verbose_name
