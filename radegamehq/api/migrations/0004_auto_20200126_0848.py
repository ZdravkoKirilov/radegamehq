# Generated by Django 2.1.1 on 2020-01-26 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200122_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stage',
            old_name='computed_slots',
            new_name='slot_getter',
        ),
        migrations.AddField(
            model_name='stage',
            name='frame_getter',
            field=models.TextField(blank=True, null=True),
        ),
    ]
