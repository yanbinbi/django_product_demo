# coding: utf-8
from django.db import models

# Create your models here.
# 用户注册
class User(models.Model):
    email = models.EmailField("邮箱")
    phone = models.IntegerField("手机号", default=0000000000)
    password = models.CharField("密码", max_length=255)


# 商品
class Product(models.Model):
    product_name = models.CharField("商品名称", max_length=50)
    product_price = models.DecimalField("商品价格", decimal_places=2, max_digits=8)

    def __str__(self):
        return self.product_name
