# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-17 23:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaf_Api', '0002_equipment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='jerseyNumber',
        ),
    ]
