# Generated by Django 2.1.1 on 2019-10-21 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20191021_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='handler',
            name='sound',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='handler_sound', to='api.Expression'),
        ),
    ]