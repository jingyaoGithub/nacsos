# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-11 09:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0097_auto_20170511_0946'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='emailtokens',
            unique_together=set([('email', 'AU')]),
        ),
        migrations.AlterIndexTogether(
            name='emailtokens',
            index_together=set([('email', 'AU')]),
        ),
    ]