# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swingtime', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SSIPEvent',
            fields=[
                ('event_ptr', models.OneToOneField(primary_key=True, auto_created=True, serialize=False, to='swingtime.Event', parent_link=True)),
                ('organizer', models.TextField(null=True, blank=True)),
                ('default_location', models.ForeignKey(null=True, to='events.Location')),
            ],
            options={
                'verbose_name': 'Actual Event',
                'verbose_name_plural': 'Actual Events',
            },
            bases=('swingtime.event',),
        ),
        migrations.CreateModel(
            name='SSIPOccurrence',
            fields=[
                ('occurrence_ptr', models.OneToOneField(primary_key=True, auto_created=True, serialize=False, to='swingtime.Occurrence', parent_link=True)),
                ('organizer', models.TextField(null=True, blank=True)),
                ('information', models.TextField(null=True, blank=True)),
                ('location', models.ForeignKey(null=True, to='events.Location')),
            ],
            options={
                'verbose_name': 'Actual Occurrence',
                'verbose_name_plural': 'Actual Occurrences',
            },
            bases=('swingtime.occurrence',),
        ),
    ]
