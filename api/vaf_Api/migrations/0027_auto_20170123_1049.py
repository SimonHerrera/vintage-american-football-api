# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-23 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaf_Api', '0026_auto_20170123_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='imageInfo',
            field=models.CharField(default='Photo Information', max_length=100),
        ),
    ]