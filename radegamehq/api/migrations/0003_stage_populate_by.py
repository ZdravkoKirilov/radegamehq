# Generated by Django 2.1.1 on 2019-08-16 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190814_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='populate_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Expression'),
        ),
    ]
