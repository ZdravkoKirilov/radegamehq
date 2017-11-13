# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 14:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20171113_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='maplocation',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='maplocation',
            name='field',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.BoardField'),
        ),
    ]