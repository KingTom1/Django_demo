from __future__ import unicode_literals
from django.db import models
# -*- coding: utf-8 -*-
# 实例化数据库中表的字段
# 自动将表生成到数据库中,manage.py makemigrations  -->manage.py migrate
class User(models.Model):
    manager = models.IntegerField(max_length=10)
    name = models.CharField(max_length=50)
    ms = models.CharField(max_length=200)
    type = models.IntegerField(max_length=10)
    stop = models.IntegerField(max_length=23)
    addDate = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     db_table = ''


# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.book_name

