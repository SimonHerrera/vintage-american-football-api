# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-26 06:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaf_Api', '0009_auto_20161026_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='image',
            field=models.ImageField(default='team_images/default_team_image.jpg', upload_to='team_images/'),
        ),
        migrations.AddField(
            model_name='team',
            name='playerId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='players', to='vaf_Api.Player'),
        ),
        migrations.AddField(
            model_name='team',
            name='year',
            field=models.IntegerField(choices=[(2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019)], default=2015),
        ),
    ]
