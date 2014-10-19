# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=32, verbose_name='title')),
                ('description', models.CharField(max_length=100, verbose_name='description')),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
                'ordering': ('title',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('abbr', models.CharField(unique=True, max_length=4, verbose_name='abbreviation')),
                ('label', models.CharField(max_length=50, verbose_name='label')),
            ],
            options={
                'verbose_name': 'event type',
                'verbose_name_plural': 'event types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('note', models.TextField(verbose_name='note')),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('object_id', models.PositiveIntegerField(verbose_name='object id')),
                ('content_type', models.ForeignKey(verbose_name='content type', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'note',
                'verbose_name_plural': 'notes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Occurrence',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('start_time', models.DateTimeField(verbose_name='start time')),
                ('end_time', models.DateTimeField(verbose_name='end time')),
                ('event', models.ForeignKey(editable=False, verbose_name='event', to='swingtime.Event')),
            ],
            options={
                'verbose_name': 'occurrence',
                'verbose_name_plural': 'occurrences',
                'ordering': ('start_time', 'end_time'),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(verbose_name='event type', to='swingtime.EventType'),
            preserve_default=True,
        ),
    ]
