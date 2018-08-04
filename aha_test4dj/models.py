from django.db import models

# Create your models here.

#发布会表
class Event(models.Model):
    name = models.CharField(max_length=100,verbose_name='发布会标题')
    limit = models.CharField(verbose_name='参加人数')
    status = models.CharField(verbose_name='状态')
    address = models.CharField(max_length=200,verbose_name='地址')
    start_time = models.DateTimeField('events time',verbose_name='发布会时间')
    create_time = models.DateTimeField(auto_now=True,verbose_name='创建时间（自动获取当前时间）')

    def __str__(self):
        return self.name

#嘉宾表
class Guest(models.Model):
    event = models.ForeignKey(Event) #关联发布会id
    realname = models.CharField(max_length=64,verbose_name='姓名')
    phone = models.CharField(max_length=16,verbose_name='手机号')
    email = models.EmailField('邮件')
    sign = models.BooleanField('签收状态')
    create_time = models.DateTimeField(auto_now=True,verbose_name='创建时间')

    class Meta:
        unique_together=("event","phone")

    def __str__(self):
        return self.realname