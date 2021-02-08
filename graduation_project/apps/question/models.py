from django.db import models
from home.baseModel import BaseModel

# Create your models here.
from user.models import Teacher


class Question(BaseModel):
    ANSWER = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )
    LEVEL = {
        ('1', 'easy'),
        ('2', 'general'),
        ('3', 'difficult'),
    }
    id = models.AutoField(primary_key=True)
    subject = models.CharField('科目', max_length=20)
    title = models.TextField('题目')
    optionA = models.CharField('A选项', max_length=30)
    optionB = models.CharField('B选项', max_length=30)
    optionC = models.CharField('C选项', max_length=30)
    optionD = models.CharField('D选项', max_length=30)
    answer = models.CharField('答案', max_length=10, choices=ANSWER)
    level = models.CharField('等级', max_length=10, choices=LEVEL)
    score = models.IntegerField('分数', default=1)

    class Meta:
        db_table = 'question'
        verbose_name = '单项选择题库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<%s:%s>' % (self.subject, self.title)


class Paper(BaseModel):
    # 题号pid 和题库为多对多的关系
    pid = models.ManyToManyField(Question)  # 多对多
    tid = models.ForeignKey(Teacher, on_delete=models.CASCADE)  # 添加外键
    subject = models.CharField('科目', max_length=20, default='')
    major = models.CharField('考卷适用专业', max_length=20)
    exam_time = models.DateTimeField()

    class Meta:
        db_table = 'paper'
        verbose_name = '试卷'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.major
