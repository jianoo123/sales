# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-23 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0015_auto_20180317_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='document_id',
            field=models.CharField(max_length=30, verbose_name='\u5355\u636e\u53f7'),
        ),
        migrations.AlterField(
            model_name='documents_tr',
            name='document_id',
            field=models.CharField(max_length=30, verbose_name='\u5355\u636e\u53f7'),
        ),
    ]
