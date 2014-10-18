# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', 'swingtime_0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventLocation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, max_length=200, editable=False)),
                ('description', models.TextField()),
                ('maphtml', models.TextField(blank=True, null=True)),
                ('directions', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Event Location',
                'verbose_name_plural': 'Event Locations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SSIPEvent',
            fields=[
                ('event_ptr', models.OneToOneField(serialize=False, primary_key=True, to='swingtime.Event', parent_link=True, auto_created=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('organizer', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
            bases=('swingtime.event',),
        ),
    ]
