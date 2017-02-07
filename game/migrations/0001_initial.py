# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='Title', max_length=255, unique=True)),
                ('description', models.TextField(default='descr')),
                ('image_url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('usertype', models.IntegerField(null=True, choices=[(0, 'Player'), (1, 'Developer')])),
                ('owned_games', models.ManyToManyField(to='game.Game')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='profile')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='creator',
            field=models.ForeignKey(to='game.Profile', related_name='created_games'),
        ),
    ]
