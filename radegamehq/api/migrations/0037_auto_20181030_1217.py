# Generated by Django 2.1.1 on 2018-10-30 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_auto_20181030_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choiceoption',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='api.Choice'),
        ),
    ]