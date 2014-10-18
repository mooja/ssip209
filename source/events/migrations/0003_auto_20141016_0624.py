# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', 'swingtime_0001_initial'),
        ('events', '0002_auto_20141016_0610'),
    ]

    operations = [
        migrations.CreateModel(
            name='SSIPOccurrence',
            fields=[
                ('occurrence_ptr', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, to='swingtime.Occurrence', auto_created=True)),
                ('location', models.ForeignKey(to='events.Location', null=True)),
            ],
            options={
            },
            bases=('swingtime.occurrence',),
        ),
        migrations.RemoveField(
            model_name='location',
            name='occurrence',
        ),
        migrations.AddField(
            model_name='ssipevent',
            name='default_location',
            field=models.ForeignKey(to='events.Location', null=True),
            preserve_default=True,
        ),
    ]
