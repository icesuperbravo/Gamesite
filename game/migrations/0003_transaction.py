# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0002_game_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('payed_game', models.ForeignKey(to='game.Game', related_name='paygame_info')),
                ('payer', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='payer_info')),
            ],
        ),
    ]
