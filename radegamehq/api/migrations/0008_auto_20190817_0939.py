# Generated by Django 2.1.1 on 2019-08-17 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20190817_0913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='condition',
        ),
        migrations.RemoveField(
            model_name='action',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='action',
            name='disable',
        ),
        migrations.RemoveField(
            model_name='action',
            name='done',
        ),
        migrations.RemoveField(
            model_name='action',
            name='enable',
        ),
        migrations.RemoveField(
            model_name='action',
            name='keywords',
        ),
        migrations.RemoveField(
            model_name='action',
            name='reveal_cost',
        ),
        migrations.RemoveField(
            model_name='action',
            name='reveal_slots',
        ),
        migrations.RemoveField(
            model_name='action',
            name='undone',
        ),
        migrations.RemoveField(
            model_name='actionconfig',
            name='action',
        ),
        migrations.RemoveField(
            model_name='actionconfig',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='actionconfig',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='actionconfig',
            name='computed_value',
        ),
        migrations.RemoveField(
            model_name='actionconfig',
            name='condition',
        ),
        migrations.RemoveField(
            model_name='actionconfig',
            name='dice_amount',
        ),
        migrations.RemoveField(
            model_name='actionconfig',
            name='faction',
        ),
        migrations.RemoveField(
            model_name='actionconfig',
            name='keywords',
        ),
        migrations.RemoveField(
            model_name='actionconfig',
            name='max_amount',
        ),
        migrations.RemoveField(
            model_name='actionconfig',
            name='min_amount',
        ),
        migrations.RemoveField(
            model_name='actionconfig',
            name='random_amount',
        ),
        migrations.RemoveField(
            model_name='actionconfig',
            name='target_filter',
        ),
        migrations.RemoveField(
            model_name='actionconfig',
            name='token',
        ),
        migrations.AddField(
            model_name='actionconfig',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='action_subject', to='api.Expression'),
        ),
        migrations.AlterField(
            model_name='actionconfig',
            name='target',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='action_target', to='api.Expression'),
        ),
        migrations.AlterField(
            model_name='actionconfig',
            name='value',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='action_value', to='api.Expression'),
        ),
    ]
