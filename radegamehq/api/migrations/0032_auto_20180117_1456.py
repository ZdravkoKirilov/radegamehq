# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_auto_20180117_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionconfig',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
