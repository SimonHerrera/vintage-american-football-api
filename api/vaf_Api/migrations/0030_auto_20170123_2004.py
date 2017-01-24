# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-24 02:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaf_Api', '0029_franchise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='playerId',
        ),
        migrations.AddField(
            model_name='team',
            name='playerId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='playerId', to='vaf_Api.Player'),
        ),
    ]
