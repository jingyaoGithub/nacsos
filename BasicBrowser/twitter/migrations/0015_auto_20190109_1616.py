# Generated by Django 2.1.2 on 2019-01-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0014_auto_20181122_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='screen_name',
            field=models.CharField(max_length=50, verbose_name='Screen name'),
        ),
    ]
