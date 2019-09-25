# Generated by Django 2.1.1 on 2019-09-25 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_slot_populate_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='style',
            old_name='strokeColor',
            new_name='stroke_color',
        ),
        migrations.RenameField(
            model_name='style',
            old_name='strokeThickness',
            new_name='stroke_thickness',
        ),
        migrations.AddField(
            model_name='style',
            name='opacity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
