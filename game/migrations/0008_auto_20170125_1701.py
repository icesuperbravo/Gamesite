# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_auto_20170124_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='usertype',
            field=models.IntegerField(null=True, choices=[(0, 'Player'), (1, 'Developer')]),
        ),
    ]
