# Generated by Django 2.2 on 2019-04-26 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0276_auto_20190426_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studyeffect',
            name='editing_time',
        ),
    ]
