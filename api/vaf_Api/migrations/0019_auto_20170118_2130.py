# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-19 03:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaf_Api', '0018_team_manager'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='manager',
            new_name='managers',
        ),
    ]
