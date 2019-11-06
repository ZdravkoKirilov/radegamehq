# Generated by Django 2.1.1 on 2019-11-05 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_auto_20191103_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='style',
            name='frame',
        ),
        migrations.RemoveField(
            model_name='style',
            name='hidden',
        ),
        migrations.AddField(
            model_name='animationstep',
            name='from_style_inline',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='animationstep',
            name='to_style_inline',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='style',
            name='background_color',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='style',
            name='border_radius',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='style',
            name='font_family',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='style',
            name='font_size',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='style',
            name='font_style',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='style',
            name='skew',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='style',
            name='x',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='style',
            name='y',
            field=models.TextField(blank=True, null=True),
        ),
    ]
