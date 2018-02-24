# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-24 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0052_auto_20180222_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Termination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('WIN', 'WIN'), ('LOSE', 'LOSE')], max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='boardType',
        ),
        migrations.AddField(
            model_name='game',
            name='hide_factions',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to='game_images'),
        ),
        migrations.AddField(
            model_name='game',
            name='main_stage',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_stage', to='api.Stage'),
        ),
        migrations.AddField(
            model_name='quest',
            name='stage',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quest_stage', to='api.Stage'),
        ),
        migrations.AddField(
            model_name='round',
            name='stage',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='round_stage', to='api.Stage'),
        ),
    ]
