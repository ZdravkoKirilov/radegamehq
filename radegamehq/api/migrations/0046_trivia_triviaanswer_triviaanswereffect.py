# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-10 19:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0045_auto_20180202_0909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trivia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.FileField(blank=True, max_length=200, null=True, upload_to='trivia_images')),
                ('mode', models.CharField(max_length=255)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
            ],
        ),
        migrations.CreateModel(
            name='TriviaAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.FileField(blank=True, max_length=200, null=True, upload_to='trivia_answer_images')),
                ('trivia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trivia_answer', to='api.Trivia')),
            ],
        ),
        migrations.CreateModel(
            name='TriviaAnswerEffect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Activity')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trivia_answer_result', to='api.TriviaAnswer')),
            ],
        ),
    ]
