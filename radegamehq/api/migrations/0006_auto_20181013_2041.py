# Generated by Django 2.1.1 on 2018-10-13 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20181013_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='options',
            field=models.ManyToManyField(related_name='choice_options', to='api.ChoiceOption'),
        ),
        migrations.AlterField(
            model_name='effectgroup',
            name='mode',
            field=models.TextField(choices=[('DRAW', 'DRAW'), ('AUTO_TRIGGER', 'AUTO_TRIGGER')], default='DRAW'),
        ),
    ]
