# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-26 07:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaf_Api', '0011_team_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='new',
        ),
    ]