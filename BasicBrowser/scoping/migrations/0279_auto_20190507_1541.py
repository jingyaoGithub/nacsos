# Generated by Django 2.2 on 2019-05-07 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0278_auto_20190507_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyeffect',
            name='significance_bound',
            field=models.IntegerField(choices=[(1, 'Lower bound'), (2, 'Upper bound'), (3, 'Actual')], null=True),
        ),
        migrations.AddField(
            model_name='studyeffect',
            name='study_design',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='aggregation_level',
            field=models.TextField(default='-999', null=True),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='calculations_file',
            field=models.FileField(blank=True, help_text='If you have made some calculations, upload them in a file here', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='coefficient',
            field=models.FloatField(default=-999, null=True),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='coefficient_sd',
            field=models.FloatField(default=-999, null=True, verbose_name='Standard error'),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='coefficient_sd_type',
            field=models.TextField(default='-999', null=True, verbose_name='Standard error type'),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='control_sample_size',
            field=models.IntegerField(default=-999, null=True),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='diff_mean',
            field=models.FloatField(blank=True, help_text='treatment - control', null=True),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='geographic_location',
            field=models.TextField(default='-999', null=True),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='geographic_scope',
            field=models.TextField(default='-999'),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='p_value',
            field=models.FloatField(default=-999),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='page',
            field=models.SmallIntegerField(default=-999),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='test_statistic',
            field=models.FloatField(default=-999, null=True),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='test_statistic_df',
            field=models.IntegerField(default=-999, null=True),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='total_sample_size',
            field=models.IntegerField(default=-999, null=True),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='treatment_sample_size',
            field=models.IntegerField(default=-999, null=True),
        ),
    ]
