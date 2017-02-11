# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='price',
            field=models.DecimalField(default=2.33, max_digits=9, decimal_places=2),
            preserve_default=False,
        ),
    ]
