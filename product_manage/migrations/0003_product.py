# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_manage', '0002_auto_20170910_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, verbose_name='商品名称')),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='商品价格')),
            ],
        ),
    ]