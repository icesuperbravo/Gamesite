# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='price',
            field=models.DecimalField(default=float, decimal_places=2, max_digits=9),
            preserve_default=False,
        ),
    ]
