# Generated by Django 2.1.1 on 2019-02-16 16:55

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('reveal_slots', models.IntegerField(blank=True, null=True)),
                ('mode', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ActionConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('target', models.CharField(max_length=255)),
                ('target_filter', models.CharField(blank=True, max_length=255, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('value', models.CharField(blank=True, max_length=255, null=True)),
                ('computed_value', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.IntegerField(blank=True, default=0, null=True)),
                ('max_amount', models.IntegerField(blank=True, default=0, null=True)),
                ('min_amount', models.IntegerField(blank=True, default=0, null=True)),
                ('random_amount', models.BooleanField(blank=True, default=False, null=True)),
                ('action', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='action_config_action', to='api.Action')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('reveal_slots', models.IntegerField(blank=True, null=True)),
                ('mode', models.CharField(max_length=255)),
                ('random', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChoiceOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('value', models.CharField(blank=True, max_length=255, null=True)),
                ('secret', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('reveal_slots', models.IntegerField(blank=True, null=True)),
                ('mode', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConditionClause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_clause', models.CharField(max_length=255)),
                ('secondary_clause', models.CharField(blank=True, max_length=255, null=True)),
                ('negative', models.BooleanField(blank=True, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('relation', models.TextField(blank=True, null=True)),
                ('action', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Action')),
                ('choice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Choice')),
                ('condition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clause_condition', to='api.Condition')),
            ],
        ),
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='game_images')),
                ('description', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_auth.AppUser')),
            ],
        ),
        migrations.CreateModel(
            name='ImageAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='images')),
                ('svg', models.FileField(blank=True, null=True, upload_to='svg_images')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game', to='api.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('turn_cycles', models.IntegerField(blank=True, default=1, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ImageAsset')),
                ('settings', models.ManyToManyField(blank=True, related_name='settings_phases', to='api.Condition')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('replay_count', models.IntegerField(blank=True, null=True)),
                ('repeat', models.IntegerField(blank=True, null=True)),
                ('phase_order', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Setup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('min_players', models.IntegerField(blank=True, null=True)),
                ('max_players', models.IntegerField(blank=True, null=True)),
                ('recommended_age', models.IntegerField(blank=True, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='setups', to='api.Game')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ImageAsset')),
                ('settings', models.ManyToManyField(blank=True, related_name='settings_setups', to='api.Condition')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('shape', models.CharField(blank=True, max_length=255, null=True)),
                ('points', models.CharField(blank=True, max_length=510, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('mode', models.TextField(choices=[('DRAW', 'DRAW'), ('AUTO', 'AUTO'), ('PASSIVE', 'PASSIVE')], default='DRAW')),
                ('pick', models.CharField(choices=[('RANDOM', 'RANDOM'), ('CHOICE', 'CHOICE')], default='RANDOM', max_length=255)),
                ('quota', models.CharField(choices=[('ONCE', 'ONCE'), ('ON_TURN', 'ON_TURN'), ('ON_PHASE', 'ON_PHASE'), ('ON_ROUND', 'ON_ROUND')], default='ONCE', max_length=255)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ImageAsset')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SourceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1)),
                ('relation', models.CharField(choices=[('NONE', 'NONE'), ('AND', 'AND'), ('OR', 'OR')], default='NONE', max_length=255)),
                ('action', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Action')),
                ('choice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Choice')),
                ('condition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Condition')),
                ('cost', models.ManyToManyField(blank=True, related_name='cost_sourceitems', to='api.Source')),
                ('disable', models.ManyToManyField(blank=True, related_name='disable_sourceitems', to='api.Condition')),
                ('enable', models.ManyToManyField(blank=True, related_name='enable_sourceitems', to='api.Condition')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='api.Source')),
                ('source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Source')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ImageAsset')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('board', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='board_teams', to='api.Stage')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ImageAsset')),
                ('settings', models.ManyToManyField(blank=True, related_name='settings_teams', to='api.Condition')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('reveal_slots', models.IntegerField(blank=True, null=True)),
                ('attributes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attributes', to='api.Source')),
                ('cost', models.ManyToManyField(blank=True, related_name='cost_tokens', to='api.Source')),
                ('disable', models.ManyToManyField(blank=True, related_name='disable_tokens', to='api.Condition')),
                ('enable', models.ManyToManyField(blank=True, related_name='enable_tokens', to='api.Condition')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ImageAsset')),
                ('reveal_cost', models.ManyToManyField(blank=True, related_name='reveal_cost_tokens', to='api.Source')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='sourceitem',
            name='token',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Token'),
        ),
        migrations.AddField(
            model_name='slot',
            name='board',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='board_slots', to='api.Stage'),
        ),
        migrations.AddField(
            model_name='slot',
            name='disable',
            field=models.ManyToManyField(blank=True, related_name='disable_slots', to='api.Condition'),
        ),
        migrations.AddField(
            model_name='slot',
            name='draw',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='draw', to='api.Source'),
        ),
        migrations.AddField(
            model_name='slot',
            name='enable',
            field=models.ManyToManyField(blank=True, related_name='enable_slots', to='api.Condition'),
        ),
        migrations.AddField(
            model_name='slot',
            name='field',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Field'),
        ),
        migrations.AddField(
            model_name='slot',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game'),
        ),
        migrations.AddField(
            model_name='slot',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ImageAsset'),
        ),
        migrations.AddField(
            model_name='slot',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Stage'),
        ),
        migrations.AddField(
            model_name='slot',
            name='revealed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Source'),
        ),
        migrations.AddField(
            model_name='slot',
            name='risk',
            field=models.ManyToManyField(blank=True, related_name='risk_slots', to='api.Source'),
        ),
        migrations.AddField(
            model_name='slot',
            name='settings',
            field=models.ManyToManyField(blank=True, related_name='settings_slots', to='api.Condition'),
        ),
        migrations.AddField(
            model_name='round',
            name='board',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='board_rounds', to='api.Stage'),
        ),
        migrations.AddField(
            model_name='round',
            name='condition',
            field=models.ManyToManyField(blank=True, related_name='condition_rounds', to='api.Condition'),
        ),
        migrations.AddField(
            model_name='round',
            name='done',
            field=models.ManyToManyField(blank=True, related_name='done_rounds', to='api.Source'),
        ),
        migrations.AddField(
            model_name='round',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game'),
        ),
        migrations.AddField(
            model_name='round',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ImageAsset'),
        ),
        migrations.AddField(
            model_name='round',
            name='phases',
            field=models.ManyToManyField(related_name='round_phases', to='api.Phase'),
        ),
        migrations.AddField(
            model_name='round',
            name='undone',
            field=models.ManyToManyField(blank=True, related_name='undone_rounds', to='api.Source'),
        ),
        migrations.AddField(
            model_name='path',
            name='board',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='board_paths', to='api.Stage'),
        ),
        migrations.AddField(
            model_name='path',
            name='cost',
            field=models.ManyToManyField(blank=True, related_name='cost_paths', to='api.Source'),
        ),
        migrations.AddField(
            model_name='path',
            name='disable',
            field=models.ManyToManyField(blank=True, related_name='disable_paths', to='api.Condition'),
        ),
        migrations.AddField(
            model_name='path',
            name='done',
            field=models.ManyToManyField(blank=True, related_name='done_paths', to='api.Source'),
        ),
        migrations.AddField(
            model_name='path',
            name='enable',
            field=models.ManyToManyField(blank=True, related_name='enable_paths', to='api.Condition'),
        ),
        migrations.AddField(
            model_name='path',
            name='from_slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_slot', to='api.Slot'),
        ),
        migrations.AddField(
            model_name='path',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game'),
        ),
        migrations.AddField(
            model_name='path',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ImageAsset'),
        ),
        migrations.AddField(
            model_name='path',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='path_owner', to='api.Stage'),
        ),
        migrations.AddField(
            model_name='path',
            name='risk',
            field=models.ManyToManyField(blank=True, related_name='risk_paths', to='api.Source'),
        ),
        migrations.AddField(
            model_name='path',
            name='to_slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Slot'),
        ),
        migrations.AddField(
            model_name='path',
            name='undone',
            field=models.ManyToManyField(blank=True, related_name='undone_paths', to='api.Source'),
        ),
        migrations.AddField(
            model_name='field',
            name='board',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='board_fields', to='api.Stage'),
        ),
        migrations.AddField(
            model_name='field',
            name='cost',
            field=models.ManyToManyField(blank=True, related_name='cost_fields', to='api.Source'),
        ),
        migrations.AddField(
            model_name='field',
            name='done',
            field=models.ManyToManyField(blank=True, related_name='done_fields', to='api.Source'),
        ),
        migrations.AddField(
            model_name='field',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game'),
        ),
        migrations.AddField(
            model_name='field',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ImageAsset'),
        ),
        migrations.AddField(
            model_name='field',
            name='risk',
            field=models.ManyToManyField(blank=True, related_name='risk_fields', to='api.Source'),
        ),
        migrations.AddField(
            model_name='field',
            name='undone',
            field=models.ManyToManyField(blank=True, related_name='undone_fields', to='api.Source'),
        ),
        migrations.AddField(
            model_name='faction',
            name='board',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='board_factions', to='api.Stage'),
        ),
        migrations.AddField(
            model_name='faction',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game'),
        ),
        migrations.AddField(
            model_name='faction',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ImageAsset'),
        ),
        migrations.AddField(
            model_name='faction',
            name='settings',
            field=models.ManyToManyField(blank=True, related_name='settings_factions', to='api.Condition'),
        ),
        migrations.AddField(
            model_name='faction',
            name='setups',
            field=models.ManyToManyField(blank=True, related_name='setups_factions', to='api.Setup'),
        ),
        migrations.AddField(
            model_name='conditionclause',
            name='faction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Faction'),
        ),
        migrations.AddField(
            model_name='conditionclause',
            name='field',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Field'),
        ),
        migrations.AddField(
            model_name='conditionclause',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clauses', to='api.Condition'),
        ),
        migrations.AddField(
            model_name='conditionclause',
            name='path',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Path'),
        ),
        migrations.AddField(
            model_name='conditionclause',
            name='phase',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Phase'),
        ),
        migrations.AddField(
            model_name='conditionclause',
            name='round',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Round'),
        ),
        migrations.AddField(
            model_name='conditionclause',
            name='slot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Slot'),
        ),
        migrations.AddField(
            model_name='conditionclause',
            name='stage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Stage'),
        ),
        migrations.AddField(
            model_name='conditionclause',
            name='token',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Token'),
        ),
        migrations.AddField(
            model_name='condition',
            name='board',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='board_conditions', to='api.Stage'),
        ),
        migrations.AddField(
            model_name='condition',
            name='cost',
            field=models.ManyToManyField(blank=True, related_name='cost_conditions', to='api.Source'),
        ),
        migrations.AddField(
            model_name='condition',
            name='disable',
            field=models.ManyToManyField(blank=True, related_name='disable_conditions', to='api.Condition'),
        ),
        migrations.AddField(
            model_name='condition',
            name='done',
            field=models.ManyToManyField(blank=True, related_name='done_conditions', to='api.Source'),
        ),
        migrations.AddField(
            model_name='condition',
            name='enable',
            field=models.ManyToManyField(blank=True, related_name='enable_conditions', to='api.Condition'),
        ),
        migrations.AddField(
            model_name='condition',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game'),
        ),
        migrations.AddField(
            model_name='condition',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ImageAsset'),
        ),
        migrations.AddField(
            model_name='condition',
            name='reveal_cost',
            field=models.ManyToManyField(blank=True, related_name='reveal_cost_conditions', to='api.Source'),
        ),
        migrations.AddField(
            model_name='condition',
            name='undone',
            field=models.ManyToManyField(blank=True, related_name='undone_conditions', to='api.Source'),
        ),
        migrations.AddField(
            model_name='choiceoption',
            name='effect',
            field=models.ManyToManyField(blank=True, to='api.Source'),
        ),
        migrations.AddField(
            model_name='choiceoption',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ImageAsset'),
        ),
        migrations.AddField(
            model_name='choiceoption',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='options', to='api.Choice'),
        ),
        migrations.AddField(
            model_name='choiceoption',
            name='settings',
            field=models.ManyToManyField(blank=True, related_name='settings_choiceoptions', to='api.Condition'),
        ),
        migrations.AddField(
            model_name='choice',
            name='condition',
            field=models.ManyToManyField(blank=True, related_name='condition_choices', to='api.Condition'),
        ),
        migrations.AddField(
            model_name='choice',
            name='cost',
            field=models.ManyToManyField(blank=True, related_name='cost_choices', to='api.Source'),
        ),
        migrations.AddField(
            model_name='choice',
            name='disable',
            field=models.ManyToManyField(blank=True, related_name='disable_choices', to='api.Condition'),
        ),
        migrations.AddField(
            model_name='choice',
            name='done',
            field=models.ManyToManyField(blank=True, related_name='done_choices', to='api.Source'),
        ),
        migrations.AddField(
            model_name='choice',
            name='enable',
            field=models.ManyToManyField(blank=True, related_name='enable_choices', to='api.Condition'),
        ),
        migrations.AddField(
            model_name='choice',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game'),
        ),
        migrations.AddField(
            model_name='choice',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ImageAsset'),
        ),
        migrations.AddField(
            model_name='choice',
            name='reveal_cost',
            field=models.ManyToManyField(blank=True, related_name='reveal_cost_choices', to='api.Source'),
        ),
        migrations.AddField(
            model_name='choice',
            name='undone',
            field=models.ManyToManyField(blank=True, related_name='undone_choices', to='api.Source'),
        ),
        migrations.AddField(
            model_name='actionconfig',
            name='choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Choice'),
        ),
        migrations.AddField(
            model_name='actionconfig',
            name='condition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Condition'),
        ),
        migrations.AddField(
            model_name='actionconfig',
            name='dice_amount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='action_dice_amount', to='api.Choice'),
        ),
        migrations.AddField(
            model_name='actionconfig',
            name='faction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Faction'),
        ),
        migrations.AddField(
            model_name='actionconfig',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='configs', to='api.Action'),
        ),
        migrations.AddField(
            model_name='actionconfig',
            name='token',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Token'),
        ),
        migrations.AddField(
            model_name='action',
            name='condition',
            field=models.ManyToManyField(blank=True, related_name='condition_actions', to='api.Condition'),
        ),
        migrations.AddField(
            model_name='action',
            name='cost',
            field=models.ManyToManyField(blank=True, related_name='cost_actions', to='api.Source'),
        ),
        migrations.AddField(
            model_name='action',
            name='disable',
            field=models.ManyToManyField(blank=True, related_name='disable_actions', to='api.Condition'),
        ),
        migrations.AddField(
            model_name='action',
            name='done',
            field=models.ManyToManyField(blank=True, related_name='done_actions', to='api.Source'),
        ),
        migrations.AddField(
            model_name='action',
            name='enable',
            field=models.ManyToManyField(blank=True, related_name='enable_actions', to='api.Condition'),
        ),
        migrations.AddField(
            model_name='action',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game'),
        ),
        migrations.AddField(
            model_name='action',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ImageAsset'),
        ),
        migrations.AddField(
            model_name='action',
            name='reveal_cost',
            field=models.ManyToManyField(blank=True, related_name='reveal_cost_actions', to='api.Source'),
        ),
        migrations.AddField(
            model_name='action',
            name='undone',
            field=models.ManyToManyField(blank=True, related_name='undone_actions', to='api.Source'),
        ),
    ]
