# Generated by Django 2.1.1 on 2019-09-25 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20190925_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='handler',
            name='enabled',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='handler_enabled', to='api.Expression'),
        ),
    ]
