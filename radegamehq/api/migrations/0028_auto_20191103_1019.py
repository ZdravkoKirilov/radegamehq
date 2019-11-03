# Generated by Django 2.1.1 on 2019-11-03 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20191103_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlotFrame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frame_slotframes', to='api.ImageAsset')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='slot',
            name='image',
        ),
        migrations.AddField(
            model_name='slotframe',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='frames', to='api.Slot'),
        ),
    ]
