# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-28 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaf_Api', '0040_auto_20170128_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='playerInfo',
            field=models.TextField(default='', max_length=200),
        ),
    ]
