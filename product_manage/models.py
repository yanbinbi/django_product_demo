# coding: utf-8
from django.db import models

# Create your models here.
# 商品分类
class Category(models.Model):
    name = models.CharField(verbose_name="分类", max_length=10)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 关键词
class Keyword(models.Model):
    name = models.CharField(verbose_name="关键词", max_length=10)

    class Meta:
        verbose_name = "关键词"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 商品
class Product(models.Model):
    spec_type = (
        ('1', '大号'),
        ('2', '中号'),
        ('3', '小号'),
    )

    name = models.CharField(u"产品名称", max_length=10)
    spec = models.CharField("产品规格", max_length=1, choices=spec_type)
    cate = models.ForeignKey(Category, verbose_name="产品分类")
    stock = models.IntegerField("库存量", default=100),
    price = models.DecimalField("价格", default=10.00, decimal_places=2, max_digits=8)
    key = models.ManyToManyField(Keyword, verbose_name="关键词")
    desc = models.TextField("商品描述", null=True, blank=True)

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField("用户名", max_length=10)
    password = models.CharField("密码", max_length=32)
    account = models.DecimalField("账户余额", default=0, decimal_places=2, max_digits=8)
    address = models.CharField("地址", max_length=255)
    email = models.EmailField("邮箱")

    class Meta:
        verbose_name = "用户名"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username