# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20171114_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maplocation',
            name='height',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='maplocation',
            name='left',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='maplocation',
            name='top',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='maplocation',
            name='width',
            field=models.FloatField(),
        ),
    ]