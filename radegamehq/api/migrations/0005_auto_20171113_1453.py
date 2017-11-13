# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20171113_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardfield',
            name='image',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to='field_images'),
        ),
        migrations.AlterField(
            model_name='map',
            name='image',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to='maps'),
        ),
    ]
