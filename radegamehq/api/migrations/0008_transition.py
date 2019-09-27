# Generated by Django 2.1.1 on 2019-09-27 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_handler_enabled'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('trigger', models.TextField()),
                ('animation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animation', to='api.Animation')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
                ('sound', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sound', to='api.Sound')),
            ],
        ),
    ]
