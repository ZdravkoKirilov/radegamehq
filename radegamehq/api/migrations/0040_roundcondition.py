# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-31 10:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_roundaction_roundquest'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoundCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Quest')),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='round_condition', to='api.Round')),
            ],
        ),
    ]
