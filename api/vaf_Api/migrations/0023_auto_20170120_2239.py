# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-21 04:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaf_Api', '0022_team_managerid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='visitorTeam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='visitorTeam', to='vaf_Api.Team'),
        ),
    ]
