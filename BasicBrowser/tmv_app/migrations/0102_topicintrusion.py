# Generated by Django 2.1.2 on 2019-03-12 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0268_auto_20190305_1731'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tmv_app', '0101_wordintrusion'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicIntrusion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(null=True)),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoping.Doc')),
                ('intruded_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intruding_doc', to='tmv_app.Topic')),
                ('real_topics', models.ManyToManyField(to='tmv_app.Topic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
