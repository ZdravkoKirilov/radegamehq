# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-01 09:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0070_auto_20180501_0907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='factionincome',
            old_name='quantity',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='factionresource',
            old_name='quantity',
            new_name='amount',
        ),
    ]