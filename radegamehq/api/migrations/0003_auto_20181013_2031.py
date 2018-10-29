# Generated by Django 2.1.1 on 2018-10-13 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181013_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='effectgroup',
            name='player_pick',
        ),
        migrations.RemoveField(
            model_name='effectgroup',
            name='random_pick',
        ),
        migrations.AddField(
            model_name='effectgroup',
            name='pick',
            field=models.CharField(choices=[('RANDOM', 'RANDOM'), ('PLAYER', 'PLAYER')], default='RANDOM', max_length=255),
        ),
    ]