# Generated by Django 2.1.1 on 2018-10-13 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_effectgroup_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='effectgroup',
            name='items',
            field=models.ManyToManyField(related_name='effect_group_items', to='api.EffectGroupItem'),
        ),
    ]
