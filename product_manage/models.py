# coding: utf-8
from django.db import models

# Create your models here.
# 用户注册
class User(models.Model):
    email = models.EmailField("邮箱")
    phone = models.IntegerField("手机号", max_length=11, default=None)
    password = models.CharField("密码", max_length=32)