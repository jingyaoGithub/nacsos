# Generated by Django 2.1.2 on 2018-11-22 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0012_user_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='scrape_fetched',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fetched'),
        ),
    ]