# Generated by Django 2.1.1 on 2019-08-17 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_keyword_display_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='style',
            name='fill',
        ),
        migrations.RemoveField(
            model_name='style',
            name='points',
        ),
        migrations.RemoveField(
            model_name='style',
            name='radius',
        ),
        migrations.RemoveField(
            model_name='style',
            name='shape',
        ),
    ]
