# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-28 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servermanager', '0007_auto_20161128_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='cpu_core_count',
            field=models.SmallIntegerField(blank=True, default=0, verbose_name='cpu\u6838\u6570'),
        ),
        migrations.AlterField(
            model_name='server',
            name='cpu_count',
            field=models.SmallIntegerField(blank=True, default=0, verbose_name='cpu\u4e2a\u6570'),
        ),
    ]