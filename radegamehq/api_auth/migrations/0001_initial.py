# Generated by Django 2.1.1 on 2020-01-15 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(blank=True, max_length=255)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_authenticated', models.BooleanField(default=False)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('alias', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
