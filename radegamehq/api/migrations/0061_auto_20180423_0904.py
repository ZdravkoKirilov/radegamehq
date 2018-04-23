# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-23 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0060_auto_20180419_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questcost',
            name='activity',
        ),
        migrations.RemoveField(
            model_name='questcost',
            name='quest',
        ),
        migrations.AlterField(
            model_name='activityconfig',
            name='target',
            field=models.CharField(choices=[('FIELD', 'FIELD'), ('PLAYER', 'PLAYER'), ('OTHER_PLAYER', 'OTHER_PLAYER'), ('SELF', 'SELF'), ('ACTIVE_PLAYER', 'ACTIVE_PLAYER'), ('FACTION', 'FACTION'), ('KEYWORD', 'KEYWORD')], max_length=255),
        ),
        migrations.AlterField(
            model_name='activityconfig',
            name='type',
            field=models.CharField(choices=[('MOVE', 'MOVE'), ('WIN_GAME', 'WIN_GAME'), ('LOSE_GAME', 'LOSE_GAME'), ('COLLECT_RESOURCES', 'COLLECT_RESOURCES'), ('ALTER_RESOURCE', 'ALTER_RESOURCE'), ('PREPARE_RESOURCE', 'PREPARE_RESOURCE'), ('STORE_RESOURCE', 'STORE_RESOURCE'), ('REQUEST_HINT', 'REQUEST_HINT'), ('GIVE_HINT', 'GIVE_HINT'), ('DRAW', 'DRAW'), ('TRIGGER_QUEST', 'TRIGGER_QUEST'), ('TRIGGER_TRIVIA', 'TRIGGER_TRIVIA'), ('PLACE_ACTIVITIES', 'PLACE_ACTIVITIES')], max_length=255),
        ),
        migrations.DeleteModel(
            name='QuestCost',
        ),
    ]
