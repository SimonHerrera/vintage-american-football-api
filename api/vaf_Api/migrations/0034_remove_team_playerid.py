# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-24 06:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaf_Api', '0033_auto_20170123_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='playerId',
        ),
    ]
