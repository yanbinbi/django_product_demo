# coding: utf-8
from django.db import models

# Create your models here.
# 用户注册
class User(models.Model):
    email = models.EmailField("邮箱")
    phone = models.IntegerField("手机号", default=0000000000)
    password = models.CharField("密码", max_length=255)
    nickname = models.CharField(max_length=40)
    name = models.CharField("姓名")



# 地址类
class Address(models.Model):
    content = models.TextField("地址", max_length=255)
    user = models.ForeignKey(User, verbose_name="用户")

# 商品
class Product(models.Model):
    product_name = models.CharField("商品名称", max_length=50)
    product_price = models.DecimalField("商品价格", max_length=8)
