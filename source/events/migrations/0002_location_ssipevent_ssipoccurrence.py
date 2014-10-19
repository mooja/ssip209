# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('swingtime', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False, max_length=200)),
                ('address', models.CharField(null=True, max_length=400)),
                ('description', models.TextField()),
                ('maphtml', models.TextField(null=True, blank=True)),
                ('directions', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Locations',
                'verbose_name': 'Location',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SSIPEvent',
            fields=[
                ('event_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, to='swingtime.Event', primary_key=True)),
                ('organizer', models.TextField(null=True, blank=True)),
                ('default_location', models.ForeignKey(null=True, to='events.Location')),
            ],
            options={
                'verbose_name_plural': 'Actual Events',
                'verbose_name': 'Actual Event',
            },
            bases=('swingtime.event',),
        ),
        migrations.CreateModel(
            name='SSIPOccurrence',
            fields=[
                ('occurrence_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, to='swingtime.Occurrence', primary_key=True)),
                ('organizer', models.TextField(null=True, blank=True)),
                ('information', models.TextField(null=True, blank=True)),
                ('location', models.ForeignKey(null=True, to='events.Location')),
            ],
            options={
                'verbose_name_plural': 'Actual Occurrences',
                'verbose_name': 'Actual Occurrence',
            },
            bases=('swingtime.occurrence',),
        ),
    ]
