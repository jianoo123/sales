# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-10 23:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commodities', '0005_auto_20180311_0646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commodities',
            name='factory',
        ),
        migrations.AddField(
            model_name='factory',
            name='commodities',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='commodities.Commodities', verbose_name='\u4e61\u9547'),
        ),
    ]
