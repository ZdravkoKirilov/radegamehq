# Generated by Django 2.1.1 on 2019-04-22 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_auth', '0002_appuser_alias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='alias',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]