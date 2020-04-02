# Generated by Django 2.1.1 on 2020-04-02 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_style_scale'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenText',
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
        migrations.RemoveField(
            model_name='setup',
            name='display_name',
        ),
        migrations.AddField(
            model_name='choiceframe',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='conditionframe',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stageframe',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='token',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='template_tokens', to='api.Stage'),
        ),
        migrations.AddField(
            model_name='tokenframe',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tokentext',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='textx', to='api.Token'),
        ),
        migrations.AddField(
            model_name='tokentext',
            name='text',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Text'),
        ),
    ]
