# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-05 23:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodities', '0002_commodities_add_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodities',
            name='charge',
            field=models.IntegerField(verbose_name='\u5546\u54c1\u4ef7\u683c'),
        ),
    ]
