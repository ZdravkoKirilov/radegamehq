# Generated by Django 2.1.1 on 2020-06-11 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='style',
            old_name='z_order',
            new_name='z',
        ),
        migrations.RemoveField(
            model_name='style',
            name='interactive',
        ),
    ]