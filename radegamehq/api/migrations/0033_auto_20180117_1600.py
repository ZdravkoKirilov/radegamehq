# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 14:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_auto_20180117_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionconfig',
            name='mode',
            field=models.CharField(choices=[('TRIGGER', 'TRIGGER'), ('PASSIVE', 'PASSIVE'), ('HIDDEN', 'HIDDEN')], max_length=255),
        ),
        migrations.AlterField(
            model_name='actionconfig',
            name='resource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='config_resource', to='api.Resource'),
        ),
        migrations.AlterField(
            model_name='actionconfig',
            name='target',
            field=models.CharField(choices=[('FIELD', 'FIELD'), ('PLAYER', 'PLAYER'), ('OTHER_PLAYER', 'OTHER_PLAYER'), ('SELF', 'SELF'), ('ACTIVE_FIELD', 'ACTIVE_FIELD'), ('ACTIVE_PLAYER', 'ACTIVE_PLAYER')], max_length=255),
        ),
        migrations.AlterField(
            model_name='actionconfig',
            name='type',
            field=models.CharField(choices=[('ATTACK_FIELD', 'ATTACK_FIELD'), ('DEFEND_FIELD', 'DEFEND_FIELD'), ('MINE_RESOURCES', 'MINE_RESOURCES'), ('CANCEL_ATTACK_FIELD', 'CANCEL_ATTACK_FIELD'), ('CANCEL_DEFEND_FIELD', 'CANCEL_DEFEND_FIELD'), ('CANCEL_MINE_RESOURCE', 'CANCEL_MINE_RESOURCE'), ('ALTER_RESOURCE', 'ALTER_RESOURCE'), ('STEAL_QUEST', 'STEAL_QUEST'), ('DISCARD_QUEST', 'DISCARD_QUEST'), ('DRAW_QUEST', 'DRAW_QUEST'), ('STEAL_ACTIVITY', 'STEAL_ACTIVITY'), ('DISCARD_ACTIVITY', 'DISCARD_ACTIVITY'), ('CANCEL_ACTIVITY', 'CANCEL_ACTIVITY'), ('PEEK_QUESTS', 'PEEK_QUESTS'), ('PEEK_ACTIVITIES', 'PEEK_ACTIVITIES')], max_length=255),
        ),
    ]