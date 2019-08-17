# Generated by Django 2.1.1 on 2019-08-17 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_style_hidden'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='keyword',
        ),
        migrations.AddField(
            model_name='state',
            name='animation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Animation'),
        ),
        migrations.AlterField(
            model_name='state',
            name='sound',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Sound'),
        ),
        migrations.AlterField(
            model_name='state',
            name='style',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Style'),
        ),
    ]
