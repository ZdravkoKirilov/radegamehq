# Generated by Django 2.1.1 on 2018-10-25 10:40

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('api', '0017_effectstack_pick'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EffectStack',
            new_name='Stack',
        ),
    ]
