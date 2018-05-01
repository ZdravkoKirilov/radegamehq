# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-01 07:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0066_auto_20180501_0658'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityQuota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter', models.CharField(max_length=255)),
                ('renewable', models.BooleanField(default=False)),
                ('auto_trigger', models.BooleanField(default=False)),
                ('amount', models.IntegerField()),
                ('type', models.CharField(choices=[('DISTRIBUTED', 'DISTRIBUTED'), ('LIMITED', 'LIMITED')], max_length=255)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quota', to='api.Activity')),
            ],
        ),
        migrations.AddField(
            model_name='faction',
            name='activity_limit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faction',
            name='resource_limit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activityconfig',
            name='target',
            field=models.CharField(choices=[('PLAYER', 'PLAYER'), ('OTHER_PLAYER', 'OTHER_PLAYER'), ('SELF', 'SELF'), ('ACTIVE_PLAYER', 'ACTIVE_PLAYER'), ('FACTION', 'FACTION'), ('KEYWORD', 'KEYWORD')], max_length=255),
        ),
        migrations.AlterField(
            model_name='activityconfig',
            name='type',
            field=models.CharField(choices=[('MOVE', 'MOVE'), ('WIN_GAME', 'WIN_GAME'), ('LOSE_GAME', 'LOSE_GAME'), ('COLLECT', 'COLLECT'), ('ALTER', 'ALTER'), ('DRAW', 'DRAW'), ('TRIGGER_QUEST', 'TRIGGER_QUEST'), ('TRIGGER_TRIVIA', 'TRIGGER_TRIVIA'), ('CANCEL', 'CANCEL')], max_length=255),
        ),
        migrations.AddField(
            model_name='activityquota',
            name='faction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faction_quota', to='api.Faction'),
        ),
        migrations.AddField(
            model_name='activityquota',
            name='field',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='field_quota', to='api.Field'),
        ),
        migrations.AddField(
            model_name='activityquota',
            name='round',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='round_quota', to='api.Round'),
        ),
        migrations.AddField(
            model_name='faction',
            name='activities',
            field=models.ManyToManyField(blank=True, related_name='faction_quota', through='api.ActivityQuota', to='api.Activity'),
        ),
    ]