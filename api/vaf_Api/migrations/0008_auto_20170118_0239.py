# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-18 08:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaf_Api', '0007_auto_20170118_0227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='awayTeam',
        ),
        migrations.RemoveField(
            model_name='game',
            name='gameTitle',
        ),
        migrations.AddField(
            model_name='game',
            name='visitorTeam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='visitoTeam', to='vaf_Api.Team'),
        ),
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.DateField(),
        ),
    ]
