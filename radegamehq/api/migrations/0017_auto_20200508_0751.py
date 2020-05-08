# Generated by Django 2.1.1 on 2020-05-08 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20200507_0626'),
    ]

    operations = [
        migrations.CreateModel(
            name='WidgetNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('style', models.TextField(blank=True, null=True)),
                ('style_inline', models.TextField(blank=True, null=True)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('display_text', models.TextField(blank=True, null=True)),
                ('provide_context', models.TextField(blank=True, null=True)),
                ('consume_context', models.TextField(blank=True, null=True)),
                ('pass_to_children', models.TextField(blank=True, null=True)),
                ('item', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='SlotHandler',
            new_name='NodeHandler',
        ),
        migrations.RenameModel(
            old_name='SlotLifecycle',
            new_name='NodeLifecycle',
        ),
        migrations.RemoveField(
            model_name='faction',
            name='game',
        ),
        migrations.RemoveField(
            model_name='slot',
            name='board',
        ),
        migrations.RemoveField(
            model_name='slot',
            name='display_text_inline',
        ),
        migrations.RemoveField(
            model_name='slot',
            name='game',
        ),
        migrations.RemoveField(
            model_name='slot',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='slot',
            name='shape',
        ),
        migrations.RemoveField(
            model_name='slot',
            name='transitions',
        ),
        migrations.RenameField(
            model_name='widget',
            old_name='slot_getter',
            new_name='node_getter',
        ),
        migrations.AlterField(
            model_name='nodehandler',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='handlers', to='api.WidgetNode'),
        ),
        migrations.AlterField(
            model_name='nodelifecycle',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lifecycles', to='api.WidgetNode'),
        ),
        migrations.DeleteModel(
            name='Faction',
        ),
        migrations.DeleteModel(
            name='Slot',
        ),
        migrations.AddField(
            model_name='widgetnode',
            name='board',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='board_widgetnodes', to='api.Widget'),
        ),
        migrations.AddField(
            model_name='widgetnode',
            name='display_text_inline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Text'),
        ),
        migrations.AddField(
            model_name='widgetnode',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game'),
        ),
        migrations.AddField(
            model_name='widgetnode',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nodes', to='api.Widget'),
        ),
        migrations.AddField(
            model_name='widgetnode',
            name='shape',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Shape'),
        ),
        migrations.AddField(
            model_name='widgetnode',
            name='transitions',
            field=models.ManyToManyField(blank=True, related_name='transitionss_widgetnodes', to='api.Transition'),
        ),
    ]
