# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-10 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0049_auto_20170210_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docownership',
            name='relevant',
            field=models.IntegerField(choices=[(0, 'Unrated'), (1, 'Yes'), (2, 'No'), (3, 'Maybe'), (4, 'Other Technology')], db_index=True, default=0, verbose_name='Relevance'),
        ),
    ]