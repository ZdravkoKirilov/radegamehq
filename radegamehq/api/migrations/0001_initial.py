# Generated by Django 2.1.1 on 2020-07-30 05:03

import api.helpers.custom_file
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
            name='Animation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('delay', models.IntegerField(blank=True, null=True)),
                ('repeat', models.IntegerField(blank=True, default=0, null=True)),
                ('bidirectional', models.BooleanField(blank=True, null=True)),
                ('type', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnimationStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delay', models.IntegerField(blank=True, null=True)),
                ('easing', models.CharField(max_length=255)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('repeat', models.IntegerField(blank=True, default=0, null=True)),
                ('bidirectional', models.BooleanField(blank=True, null=True)),
                ('from_value', models.TextField(blank=True, null=True)),
                ('to_value', models.TextField(blank=True, null=True)),
                ('from_style_inline', models.TextField(blank=True, null=True)),
                ('to_style_inline', models.TextField(blank=True, null=True)),
                ('output_transformer', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='api.Animation')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChoiceFrame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.TextField(blank=True, null=True)),
                ('style_inline', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChoiceOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.TextField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChoiceTip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
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
                ('keywords', models.TextField(blank=True, null=True)),
                ('clause', models.TextField(blank=True, null=True)),
                ('passes', models.TextField(blank=True, null=True)),
                ('fails', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConditionFrame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.TextField(blank=True, null=True)),
                ('style_inline', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Expression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('preload_as', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.TextField()),
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
                ('title', models.CharField(db_index=True, max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='game_images')),
                ('description', models.TextField(blank=True, null=True)),
                ('core_data', models.TextField(blank=True, null=True)),
                ('get_active_module', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GameLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('display_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='images')),
                ('svg', models.FileField(blank=True, null=True, upload_to='svg_images')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game', to='api.Game')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('preload', models.TextField(blank=True, null=True)),
                ('load_done', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NodeHandler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('effect', models.TextField(blank=True, null=True)),
                ('sound', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NodeLifecycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('effect', models.TextField(blank=True, null=True)),
                ('sound', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sandbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('global_state', models.TextField(blank=True, null=True)),
                ('own_data', models.TextField(blank=True, null=True)),
                ('on_init', models.TextField(blank=True, null=True)),
                ('preload', models.TextField(blank=True, null=True)),
                ('load_done', models.TextField(blank=True, null=True)),
                ('from_parent', models.TextField(blank=True, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
                ('module', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Module')),
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
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('min_players', models.IntegerField(blank=True, null=True)),
                ('max_players', models.IntegerField(blank=True, null=True)),
                ('recommended_age', models.IntegerField(blank=True, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('style', models.TextField(blank=True, null=True)),
                ('style_inline', models.TextField(blank=True, null=True)),
                ('type', models.TextField()),
                ('construct_by_inline', models.TextField(blank=True, null=True)),
                ('construct_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Expression')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShapePoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.CharField(max_length=255)),
                ('y', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='points', to='api.Shape')),
            ],
        ),
        migrations.CreateModel(
            name='Sonata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('type', models.TextField()),
                ('loop', models.NullBooleanField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SonataStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.FloatField(blank=True, null=True)),
                ('loop', models.NullBooleanField()),
                ('rate', models.FloatField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='api.Sonata')),
            ],
        ),
        migrations.CreateModel(
            name='Sound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('file', api.helpers.custom_file.ContentTypeRestrictedFileField(upload_to='sounds')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('rotation', models.TextField(blank=True, null=True)),
                ('border_radius', models.TextField(blank=True, null=True)),
                ('opacity', models.TextField(blank=True, null=True)),
                ('skew', models.TextField(blank=True, null=True)),
                ('scale', models.TextField(blank=True, null=True)),
                ('width', models.TextField(blank=True, null=True)),
                ('height', models.TextField(blank=True, null=True)),
                ('y', models.TextField(blank=True, null=True)),
                ('x', models.TextField(blank=True, null=True)),
                ('z', models.IntegerField(blank=True, null=True)),
                ('stroke_color', models.TextField(blank=True, null=True)),
                ('stroke_thickness', models.TextField(blank=True, null=True)),
                ('fill', models.TextField(blank=True, null=True)),
                ('tint', models.TextField(blank=True, null=True)),
                ('font_size', models.TextField(blank=True, null=True)),
                ('font_family', models.TextField(blank=True, null=True)),
                ('font_style', models.TextField(blank=True, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('style', models.TextField(blank=True, null=True)),
                ('style_inline', models.TextField(blank=True, null=True)),
                ('default_value', models.TextField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
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
                ('keywords', models.TextField(blank=True, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TokenFrame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.TextField(blank=True, null=True)),
                ('style_inline', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image_tokenframes', to='api.ImageAsset')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='frames', to='api.Token')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TokenText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.TextField(blank=True, null=True)),
                ('style_inline', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='texts', to='api.Token')),
                ('text', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Text')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('trigger', models.TextField()),
                ('sound', models.TextField(blank=True, null=True)),
                ('enabled', models.TextField(blank=True, null=True)),
                ('animation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animation', to='api.Animation')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.GameLanguage')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='api.Text')),
            ],
        ),
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('style', models.TextField(blank=True, null=True)),
                ('style_inline', models.TextField(blank=True, null=True)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('node_getter', models.TextField(blank=True, null=True)),
                ('render', models.TextField(blank=True, null=True)),
                ('frame_getter', models.TextField(blank=True, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WidgetFrame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.TextField(blank=True, null=True)),
                ('style_inline', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image_widgetframes', to='api.ImageAsset')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='frames', to='api.Widget')),
                ('widget', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='widget_widgetframes', to='api.Widget')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WidgetNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('style', models.TextField(blank=True, null=True)),
                ('style_inline', models.TextField(blank=True, null=True)),
                ('display_text', models.TextField(blank=True, null=True)),
                ('provide_context', models.TextField(blank=True, null=True)),
                ('consume_context', models.TextField(blank=True, null=True)),
                ('pass_to_children', models.TextField(blank=True, null=True)),
                ('item', models.TextField(blank=True, null=True)),
                ('board', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='board_widgetnodes', to='api.Widget')),
                ('display_text_inline', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Text')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
                ('module', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Module')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nodes', to='api.Widget')),
                ('shape', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Shape')),
                ('transitions', models.ManyToManyField(blank=True, related_name='transitionss_widgetnodes', to='api.Transition')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='tokenframe',
            name='widget',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='widget_tokenframes', to='api.Widget'),
        ),
        migrations.AddField(
            model_name='token',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='template_tokens', to='api.Widget'),
        ),
        migrations.AddField(
            model_name='sonatastep',
            name='sound',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Sound'),
        ),
        migrations.AddField(
            model_name='sandbox',
            name='node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.WidgetNode'),
        ),
        migrations.AddField(
            model_name='sandbox',
            name='widget',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Widget'),
        ),
        migrations.AddField(
            model_name='nodelifecycle',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lifecycles', to='api.WidgetNode'),
        ),
        migrations.AddField(
            model_name='nodelifecycle',
            name='static_sound',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Sonata'),
        ),
        migrations.AddField(
            model_name='nodehandler',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='handlers', to='api.WidgetNode'),
        ),
        migrations.AddField(
            model_name='nodehandler',
            name='static_sound',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Sonata'),
        ),
        migrations.AddField(
            model_name='module',
            name='board',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='board_modules', to='api.Widget'),
        ),
        migrations.AddField(
            model_name='module',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game'),
        ),
        migrations.AddField(
            model_name='module',
            name='loader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Widget'),
        ),
        migrations.AddField(
            model_name='gamelanguage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ImageAsset'),
        ),
        migrations.AddField(
            model_name='gamelanguage',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='api.Game'),
        ),
        migrations.AddField(
            model_name='game',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='menu', to='api.Widget'),
        ),
        migrations.AddField(
            model_name='game',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_auth.AppUser'),
        ),
        migrations.AddField(
            model_name='expression',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game'),
        ),
        migrations.AddField(
            model_name='conditionframe',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image_conditionframes', to='api.ImageAsset'),
        ),
        migrations.AddField(
            model_name='conditionframe',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='frames', to='api.Condition'),
        ),
        migrations.AddField(
            model_name='conditionframe',
            name='widget',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='widget_conditionframes', to='api.Widget'),
        ),
        migrations.AddField(
            model_name='condition',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game'),
        ),
        migrations.AddField(
            model_name='condition',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='template_conditions', to='api.Widget'),
        ),
        migrations.AddField(
            model_name='choicetip',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ImageAsset'),
        ),
        migrations.AddField(
            model_name='choicetip',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tips', to='api.Choice'),
        ),
        migrations.AddField(
            model_name='choiceoption',
            name='effect',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Expression'),
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
            model_name='choiceframe',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image_choiceframes', to='api.ImageAsset'),
        ),
        migrations.AddField(
            model_name='choiceframe',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='frames', to='api.Choice'),
        ),
        migrations.AddField(
            model_name='choiceframe',
            name='widget',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='widget_choiceframes', to='api.Widget'),
        ),
        migrations.AddField(
            model_name='choice',
            name='chances',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='choice_chances', to='api.Expression'),
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
            name='options_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='choice_options_filter', to='api.Expression'),
        ),
        migrations.AddField(
            model_name='choice',
            name='scope',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='choice_scope', to='api.Expression'),
        ),
        migrations.AddField(
            model_name='choice',
            name='time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='choice_time', to='api.Expression'),
        ),
        migrations.AddField(
            model_name='animation',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game'),
        ),
    ]
