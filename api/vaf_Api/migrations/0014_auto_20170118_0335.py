# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-18 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaf_Api', '0013_auto_20170118_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='year',
            field=models.IntegerField(choices=[(2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019)], default=2015),
        ),
    ]
