# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 10:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_auto_20180116_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionconfig',
            name='resource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='config_resource', to='api.Action'),
        ),
    ]