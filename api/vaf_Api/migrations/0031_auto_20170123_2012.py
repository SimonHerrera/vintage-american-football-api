# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-24 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaf_Api', '0030_auto_20170123_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='playerId',
        ),
        migrations.AddField(
            model_name='team',
            name='playerId',
            field=models.ManyToManyField(to='vaf_Api.Player'),
        ),
    ]
