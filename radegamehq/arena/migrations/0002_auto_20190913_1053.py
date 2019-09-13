# Generated by Django 2.1.1 on 2019-09-13 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arena', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameplayer',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='arena.GameInstance'),
        ),
    ]
