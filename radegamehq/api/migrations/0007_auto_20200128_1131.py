# Generated by Django 2.1.1 on 2020-01-28 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_style_z_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='condition',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='template_conditions', to='api.Stage'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='clause',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='condition',
            name='fails',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='condition',
            name='passes',
            field=models.TextField(blank=True, null=True),
        ),
    ]