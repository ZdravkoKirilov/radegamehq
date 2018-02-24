# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-25 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_auto_20180124_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questaward',
            name='type',
            field=models.CharField(choices=[('RESOURCE', 'RESOURCE'), ('RANDOM_RESOURCE', 'RANDOM_RESOURCE')], max_length=255),
        ),
        migrations.AlterField(
            model_name='questcondition',
            name='type',
            field=models.CharField(choices=[('CLAIM_FIELD', 'CLAIM_FIELD'), ('CLAIM_ANY_FIELDS', 'CLAIM_ANY_FIELDS'), ('DEFEND_FIELD', 'DEFEND_FIELD'), ('DEFEND_ANY_FIELDS', 'DEFEND_ANY_FIELDS'), ('CLAIM_RESOURCE', 'CLAIM_RESOURCE'), ('CLAIM_ANY_RESOURCE', 'CLAIM_ANY_RESOURCE'), ('STEAL_ACTIVITY', 'STEAL_ACTIVITY'), ('STEAL_ANY_ACTIVITY', 'STEAL_ANY_ACTIVITY'), ('DISCARD_ACTIVITY', 'DISCARD_ACTIVITY'), ('DISCARD_ANY_ACTIVITY', 'DISCARD_ANY_ACTIVITY'), ('PLAY_ACTIVITY', 'PLAY_ACTIVITY'), ('PLAY_ANY_ACTIVITY', 'PLAY_ANY_ACTIVITY')], max_length=255),
        ),
        migrations.AlterField(
            model_name='questcost',
            name='type',
            field=models.CharField(choices=[('RESOURCE', 'RESOURCE'), ('FIELD', 'FIELD')], max_length=255),
        ),
        migrations.AlterField(
            model_name='questpenalty',
            name='type',
            field=models.CharField(choices=[('RESOURCE', 'RESOURCE'), ('RANDOM_RESOURCE', 'RANDOM_RESOURCE')], max_length=255),
        ),
    ]