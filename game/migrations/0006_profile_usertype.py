# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='usertype',
            field=models.IntegerField(choices=[(1, 'Player'), (2, 'Developer')], default=1),
        ),
    ]
