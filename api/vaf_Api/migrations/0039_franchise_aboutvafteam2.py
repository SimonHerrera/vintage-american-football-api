# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-28 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaf_Api', '0038_team_franchiseid'),
    ]

    operations = [
        migrations.AddField(
            model_name='franchise',
            name='aboutVafTeam2',
            field=models.TextField(default='', max_length=400),
        ),
    ]