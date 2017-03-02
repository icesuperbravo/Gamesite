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
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=255, default='Title')),
                ('description', models.TextField(default='descr')),
                ('image_url', models.URLField(blank=True)),
                ('game_url', models.URLField(unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('usertype', models.IntegerField(choices=[(0, 'Player'), (1, 'Developer')], null=True)),
                ('owned_games', models.ManyToManyField(to='game.Game')),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Save',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('highscore', models.IntegerField()),
                ('game', models.ForeignKey(related_name='saves', to='game.Game')),
                ('player', models.ForeignKey(to='game.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('date', models.DateTimeField(auto_now=True)),
                ('payed_game', models.ForeignKey(related_name='paygame_info', to='game.Game')),
                ('payer', models.ForeignKey(related_name='payer_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='creator',
            field=models.ForeignKey(related_name='created_games', to='game.Profile'),
        ),
        migrations.AlterUniqueTogether(
            name='save',
            unique_together=set([('player', 'game')]),
        ),
    ]
