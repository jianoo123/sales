# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-15 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0006_auto_20180314_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documents',
            name='salescharge',
        ),
        migrations.AddField(
            model_name='documents',
            name='charge',
            field=models.CharField(default=340, max_length=10, verbose_name='\u5546\u54c1\u4ef7\u683c'),
            preserve_default=False,
        ),
    ]
