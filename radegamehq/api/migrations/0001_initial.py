# Generated by Django 2.1.1 on 2018-10-13 20:21

from django.db import migrations, models
import django.db.models.deletion


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
                ('description', models.TextField(blank=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='action_images')),
                ('restriction', models.TextField(blank=True, null=True)),
                ('trap_mode', models.BooleanField(default=False, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ActionConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('MOVE', 'MOVE'), ('WIN_GAME', 'WIN_GAME'), ('LOSE_GAME', 'LOSE_GAME'), ('COLLECT', 'COLLECT'), ('ALTER', 'ALTER'), ('DRAW', 'DRAW'), ('TRIGGER_QUEST', 'TRIGGER_QUEST'), ('TRIGGER_TRIVIA', 'TRIGGER_TRIVIA'), ('CANCEL', 'CANCEL'), ('REDIRECT', 'REDIRECT')], max_length=255)),
                ('target', models.CharField(choices=[('PLAYER', 'PLAYER'), ('OTHER_PLAYER', 'OTHER_PLAYER'), ('SELF', 'SELF'), ('ACTIVE_PLAYER', 'ACTIVE_PLAYER'), ('FACTION', 'FACTION'), ('KEYWORD', 'KEYWORD')], max_length=255)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, max_length=200, null=True, upload_to='choice_images')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChoiceOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, max_length=200, null=True, upload_to='choice_option_images')),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='condition_images')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConditionClause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('CLAIM', 'CLAIM'), ('REACH', 'REACH'), ('MEET', 'MEET'), ('AVOID', 'AVOID'), ('COMPLETE', 'COMPLETE'), ('TRIGGER', 'TRIGGER'), ('GATHER', 'GATHER')], max_length=255)),
                ('keyword', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('action', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='condition_clause_action', to='api.Action')),
            ],
        ),
        migrations.CreateModel(
            name='EffectGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.TextField(choices=[('DRAW', 'DRAW'), ('AUTO_TRIGGER', 'AUTO_TRIGGER')])),
                ('random_pick', models.BooleanField(default=False)),
                ('player_pick', models.BooleanField(default=True)),
                ('min_cap', models.IntegerField(blank=True, null=True)),
                ('max_cap', models.IntegerField(blank=True, null=True)),
                ('random_cap', models.BooleanField(default=False)),
                ('allow_same_pick', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EffectGroupItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quota', models.IntegerField(default=1)),
                ('restriction', models.TextField(blank=True, null=True)),
                ('action', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Action')),
                ('condition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Condition')),
            ],
        ),
        migrations.CreateModel(
            name='EffectStack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.TextField(choices=[('AND', 'AND'), ('OR', 'OR')], default='AND')),
                ('action', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Action')),
                ('condition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Condition')),
            ],
        ),
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.FileField(blank=True, max_length=255, null=True, upload_to='faction_images')),
                ('type', models.CharField(choices=[('PLAYER', 'PLAYER'), ('BOT', 'BOT'), ('MASTER', 'MASTER')], default='PLAYER', max_length=255)),
                ('activity_limit', models.IntegerField(blank=True, null=True)),
                ('resource_limit', models.IntegerField(blank=True, null=True)),
                ('effect_pool', models.ManyToManyField(related_name='faction_effect_pool', to='api.EffectGroup')),
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
                ('description', models.TextField(blank=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.FileField(blank=True, max_length=255, null=True, upload_to='field_images')),
                ('award', models.ManyToManyField(related_name='field_award', to='api.EffectStack')),
                ('cost', models.ManyToManyField(related_name='field_cost', to='api.EffectStack')),
                ('effect_pool', models.ManyToManyField(related_name='field_effect_pool', to='api.EffectGroup')),
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
                ('min_players', models.IntegerField(blank=True, null=True)),
                ('max_players', models.IntegerField(blank=True, null=True)),
                ('recommended_age', models.CharField(blank=True, max_length=255, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_auth.AppUser')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Field')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_loc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='path_from_loc', to='api.Location')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.FileField(blank=True, max_length=200, null=True, upload_to='resource_images')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
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
                ('description', models.TextField(blank=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='round_images')),
                ('replay_count', models.IntegerField(blank=True, null=True)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('award', models.ManyToManyField(related_name='round_award', to='api.EffectStack')),
                ('condition', models.ManyToManyField(related_name='round_condition', to='api.EffectStack')),
                ('effect_pool', models.ManyToManyField(related_name='round_effect_pool', to='api.EffectGroup')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
                ('penalty', models.ManyToManyField(related_name='round_penalty', to='api.EffectStack')),
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
                ('description', models.TextField(blank=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.FileField(blank=True, max_length=255, null=True, upload_to='stage_images')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='round',
            name='stage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='round_stage', to='api.Stage'),
        ),
        migrations.AddField(
            model_name='path',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Stage'),
        ),
        migrations.AddField(
            model_name='path',
            name='to_loc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='path_to_loc', to='api.Location'),
        ),
        migrations.AddField(
            model_name='location',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Stage'),
        ),
        migrations.AddField(
            model_name='field',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game'),
        ),
        migrations.AddField(
            model_name='field',
            name='penalty',
            field=models.ManyToManyField(related_name='field_penalty', to='api.EffectStack'),
        ),
        migrations.AddField(
            model_name='field',
            name='stage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Stage'),
        ),
        migrations.AddField(
            model_name='faction',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game'),
        ),
        migrations.AddField(
            model_name='faction',
            name='start',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Location'),
        ),
        migrations.AddField(
            model_name='effectstack',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game'),
        ),
        migrations.AddField(
            model_name='effectgroupitem',
            name='cost',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.EffectStack'),
        ),
        migrations.AddField(
            model_name='effectgroupitem',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.EffectGroup'),
        ),
        migrations.AddField(
            model_name='effectgroup',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game'),
        ),
        migrations.AddField(
            model_name='conditionclause',
            name='at_round',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='condition_clause_atround', to='api.Round'),
        ),
        migrations.AddField(
            model_name='conditionclause',
            name='by_round',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='condition_clause_byround', to='api.Round'),
        ),
        migrations.AddField(
            model_name='conditionclause',
            name='condition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='condition_clause_condition', to='api.Condition'),
        ),
        migrations.AddField(
            model_name='conditionclause',
            name='field',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='condition_clause_field', to='api.Field'),
        ),
        migrations.AddField(
            model_name='conditionclause',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='condition_clause', to='api.Condition'),
        ),
        migrations.AddField(
            model_name='conditionclause',
            name='resource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='condition_clause_resource', to='api.Resource'),
        ),
        migrations.AddField(
            model_name='condition',
            name='award',
            field=models.ManyToManyField(related_name='condition_award', to='api.EffectStack'),
        ),
        migrations.AddField(
            model_name='condition',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game'),
        ),
        migrations.AddField(
            model_name='condition',
            name='penalty',
            field=models.ManyToManyField(related_name='condition_penalty', to='api.EffectStack'),
        ),
        migrations.AddField(
            model_name='condition',
            name='stage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='condition_stage', to='api.Stage'),
        ),
        migrations.AddField(
            model_name='choiceoption',
            name='effect',
            field=models.ManyToManyField(related_name='choice_option_effects', to='api.EffectStack'),
        ),
        migrations.AddField(
            model_name='choiceoption',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_options', to='api.Choice'),
        ),
        migrations.AddField(
            model_name='choice',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game'),
        ),
        migrations.AddField(
            model_name='actionconfig',
            name='choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='action_choice', to='api.Choice'),
        ),
        migrations.AddField(
            model_name='actionconfig',
            name='condition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='action_condition', to='api.Condition'),
        ),
        migrations.AddField(
            model_name='actionconfig',
            name='faction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='action_faction', to='api.Faction'),
        ),
        migrations.AddField(
            model_name='actionconfig',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='configs', to='api.Action'),
        ),
        migrations.AddField(
            model_name='actionconfig',
            name='resource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='action_config_resource', to='api.Resource'),
        ),
        migrations.AddField(
            model_name='action',
            name='cost',
            field=models.ManyToManyField(related_name='action_cost', to='api.EffectStack'),
        ),
        migrations.AddField(
            model_name='action',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game'),
        ),
        migrations.AddField(
            model_name='action',
            name='limitation',
            field=models.ManyToManyField(related_name='action_limitation', to='api.EffectStack'),
        ),
    ]
