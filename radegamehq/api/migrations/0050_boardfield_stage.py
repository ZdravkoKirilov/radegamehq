# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-22 13:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0049_auto_20180217_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardfield',
            name='stage',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='api.Stage'),
            preserve_default=False,
        ),
    ]