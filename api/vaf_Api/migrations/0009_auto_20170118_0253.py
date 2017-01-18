# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-18 08:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaf_Api', '0008_auto_20170118_0239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default='Rock Island', max_length=40)),
                ('state', models.CharField(default='IL', max_length=2)),
                ('venueName', models.CharField(default='Douglas Park', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='city',
        ),
        migrations.RemoveField(
            model_name='game',
            name='state',
        ),
        migrations.RemoveField(
            model_name='game',
            name='venueName',
        ),
        migrations.AddField(
            model_name='game',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='vaf_Api.Location'),
        ),
    ]
