# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 08:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20171201_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.FileField(blank=True, max_length=200, null=True, upload_to='faction_images')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
            ],
        ),
        migrations.CreateModel(
            name='FactionResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField()),
                ('faction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faction_resource', to='api.Faction')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Resource')),
            ],
        ),
        migrations.AddField(
            model_name='faction',
            name='resources',
            field=models.ManyToManyField(blank=True, through='api.FactionResource', to='api.Resource'),
        ),
    ]