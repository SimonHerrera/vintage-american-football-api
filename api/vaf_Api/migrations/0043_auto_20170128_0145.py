# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-28 07:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaf_Api', '0042_auto_20170128_0106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='franchise',
            old_name='cityName',
            new_name='FranCityName',
        ),
        migrations.RenameField(
            model_name='franchise',
            old_name='teamName',
            new_name='FranTeamName',
        ),
    ]