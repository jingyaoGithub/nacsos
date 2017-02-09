# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-01 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmv_app', '0010_hdoctopic_htopic_htopicterm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='htopic',
            name='n_docs',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='htopic',
            name='n_words',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='htopic',
            name='scale',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='htopic',
            name='title',
            field=models.CharField(max_length=80, null=True),
        ),
    ]