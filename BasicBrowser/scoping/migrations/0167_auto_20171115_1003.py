# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-15 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0166_auto_20171110_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='kw',
            name='kwtype',
            field=models.IntegerField(choices=[(0, 'author'), (1, 'auto_wos')], null=True),
        ),
        migrations.AlterField(
            model_name='kw',
            name='text',
            field=models.TextField(db_index=True),
        ),
    ]