# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-11 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0056_auto_20180411_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='keywords',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]