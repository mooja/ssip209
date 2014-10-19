# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('swingtime', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, max_length=200, editable=False)),
                ('address', models.CharField(max_length=400, null=True)),
                ('description', models.TextField()),
                ('maphtml', models.TextField(blank=True, null=True)),
                ('directions', models.TextField(blank=True, null=True)),
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
                ('event_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, primary_key=True, to='swingtime.Event')),
                ('organizer', models.TextField(blank=True, null=True)),
                ('default_location', models.ForeignKey(to='events.Location', null=True)),
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
                ('occurrence_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, primary_key=True, to='swingtime.Occurrence')),
                ('organizer', models.TextField(blank=True, null=True)),
                ('information', models.TextField(blank=True, null=True)),
                ('location', models.ForeignKey(to='events.Location', null=True)),
            ],
            options={
                'verbose_name_plural': 'Actual Occurrences',
                'verbose_name': 'Actual Occurrence',
            },
            bases=('swingtime.occurrence',),
        ),
    ]
