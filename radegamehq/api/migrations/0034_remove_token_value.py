# Generated by Django 2.1.1 on 2019-11-19 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_merge_20191118_0826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='value',
        ),
    ]
