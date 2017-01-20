# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-19 03:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaf_Api', '0017_remove_team_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teams', to='vaf_Api.Manager'),
        ),
    ]
