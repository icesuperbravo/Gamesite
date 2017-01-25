# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=255)),
                ('user_passWd', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2)),
                ('name', models.CharField(blank=True, null=True, max_length=30)),
                ('birth', models.CharField(blank=True, null=True, max_length=30)),
            ],
        ),
    ]
