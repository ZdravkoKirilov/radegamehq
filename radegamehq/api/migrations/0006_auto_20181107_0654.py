# Generated by Django 2.1.1 on 2018-11-07 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_faction_stage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faction',
            name='stage',
        ),
        migrations.AddField(
            model_name='faction',
            name='boards',
            field=models.ManyToManyField(blank=True, to='api.Stage'),
        ),
    ]