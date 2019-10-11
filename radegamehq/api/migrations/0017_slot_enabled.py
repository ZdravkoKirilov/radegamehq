# Generated by Django 2.1.1 on 2019-10-03 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20191001_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='enabled',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='slot_enabled', to='api.Expression'),
        ),
    ]