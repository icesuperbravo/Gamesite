# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_passWd',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_name',
            new_name='username',
        ),
    ]
