# Generated by Django 2.1.1 on 2018-10-14 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20181014_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='trap_mode',
            field=models.NullBooleanField(default=False),
        ),
    ]