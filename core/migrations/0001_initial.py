# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gtfs_stop_id', models.IntegerField(unique=True, db_index=True)),
                ('english', models.CharField(max_length=50)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
