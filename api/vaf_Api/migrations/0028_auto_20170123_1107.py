# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-23 17:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaf_Api', '0027_auto_20170123_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='aboutOrgTeamParagraph',
        ),
        migrations.RemoveField(
            model_name='team',
            name='aboutOrgTeamParagraph2',
        ),
        migrations.RemoveField(
            model_name='team',
            name='vafEstablished',
        ),
    ]
