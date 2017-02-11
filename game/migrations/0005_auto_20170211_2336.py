# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_transaction_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Highscore',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='game_url',
            field=models.URLField(default='http://facebook.com'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='highscore',
            name='game',
            field=models.ForeignKey(related_name='highscores', to='game.Game'),
        ),
        migrations.AddField(
            model_name='highscore',
            name='player',
            field=models.ForeignKey(to='game.Profile'),
        ),
        migrations.AlterUniqueTogether(
            name='highscore',
            unique_together=set([('player', 'game')]),
        ),
    ]
