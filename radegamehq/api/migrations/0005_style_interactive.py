# Generated by Django 2.1.1 on 2020-01-28 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200126_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='style',
            name='interactive',
            field=models.NullBooleanField(),
        ),
    ]