# coding: utf-8
from django.db import models

# Create your models here.
# 用户注册
class User(models.Model):
    email = models.EmailField("邮箱")
    phone = models.IntegerField("手机号", default=0000000000)
    password = models.CharField("密码", max_length=255)
    nickname = models.CharField("昵称", max_length=40, default="nickname")
    name = models.CharField("姓名", max_length=20, default="name")
    account = models.DecimalField("账户", max_digits=10, decimal_places=2, default=0)
    address = models.TextField(max_length=255, default="")

# 商品分类
class Category(models.Model):
    name = models.CharField("商品分类", max_length=30)

    def __str__(self):
        return self.name

# 商品
class Product(models.Model):
    product_name = models.CharField("商品名称", max_length=50)
    product_price = models.DecimalField("商品价格", max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, verbose_name="商品分类")

# 条目
class LineItem(models.Model):
    product = models.ForeignKey(Product)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()

# 购物车
class Cart(object):
    def __init__(self, *args, **kwargs):
        self.items = []
        self.total_price = 0

    def add_product(self, product):
        self.total_price += product.product_price

        for item in self.items:
            if item.product.id == product.id:
                item.quantity += 1
        return self.items.append(LineItem(product=product, unit_price=product.product_price, quantity=1))
