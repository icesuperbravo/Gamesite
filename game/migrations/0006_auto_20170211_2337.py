# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20170211_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_url',
            field=models.URLField(unique=True),
        ),
    ]
