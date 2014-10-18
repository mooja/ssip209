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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, max_length=200, editable=False)),
                ('description', models.TextField()),
                ('maphtml', models.TextField(null=True, blank=True)),
                ('directions', models.TextField(null=True, blank=True)),
                ('occurrence', models.ForeignKey(to='swingtime.Occurrence')),
            ],
            options={
                'verbose_name_plural': 'Event Locations',
                'verbose_name': 'Event Location',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='EventLocation',
        ),
        migrations.RemoveField(
            model_name='ssipevent',
            name='location',
        ),
    ]
