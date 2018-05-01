# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-01 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0069_auto_20180501_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='faction',
            name='activities',
            field=models.ManyToManyField(blank=True, related_name='faction_quota', through='api.ActivityQuota', to='api.Activity'),
        ),
        migrations.AddField(
            model_name='faction',
            name='income',
            field=models.ManyToManyField(blank=True, related_name='faction_income', through='api.FactionIncome', to='api.Resource'),
        ),
        migrations.AddField(
            model_name='faction',
            name='resources',
            field=models.ManyToManyField(blank=True, through='api.FactionResource', to='api.Resource'),
        ),
        migrations.AlterField(
            model_name='faction',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]