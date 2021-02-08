from django.db import models
from home.baseModel import BaseModel

# 为性别,学院 指定备选字段
SEX = (
    ('男', '男'),
    ('女', '女'),
)
DEPT = (
    ('计算机与通信学院', '计算机与通信学院'),
    ('电气与自动化学院', '电气与自动化学院'),
    ('外国语学院', '外国语学院'),
    ('软件学院', '软件学院'),
)


# Create your models here.
class Teacher(BaseModel):
    id = models.CharField("教工号", max_length=20, primary_key=True)
    name = models.CharField('姓名', max_length=20)
    sex = models.CharField('性别', max_length=4, choices=SEX, default='男')
    dept = models.CharField('学院', max_length=20, choices=DEPT, default=None)
    email = models.EmailField('邮箱', default=None)
    password = models.CharField('密码', max_length=20, default='000000')
    birth = models.DateField('出生日期')

    class Meta:
        db_table = 'teacher'
        verbose_name = '教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Student(BaseModel):
    id = models.CharField('学号', max_length=20, primary_key=True)
    name = models.CharField('姓名', max_length=20)
    sex = models.CharField('性别', max_length=4, choices=SEX, default='男')
    dept = models.CharField('学院', max_length=20, choices=DEPT, default=None)
    major = models.CharField('专业', max_length=20, default=None)
    password = models.CharField('密码', max_length=20, default='111')
    email = models.EmailField('邮箱', default=None)
    birth = models.DateField('出生日期')

    class Meta:
        db_table = 'student'
        verbose_name = '学生'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id
