# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-16 23:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0013_auto_20180317_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents_tr',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.today, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
    ]