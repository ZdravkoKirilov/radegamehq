# Generated by Django 2.1.1 on 2019-08-30 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0004_slot_populate_by'),
        ('api_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('public_id', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.TextField(blank=True, null=True)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
            ],
        ),
        migrations.CreateModel(
            name='GamePlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('color', models.IntegerField(blank=True, null=True)),
                ('faction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Faction')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arena.GameInstance')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Team')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_auth.AppUser')),
            ],
        ),
    ]