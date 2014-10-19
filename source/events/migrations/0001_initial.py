# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False, max_length=200)),
                ('address', models.CharField(max_length=400, null=True)),
                ('description', models.TextField()),
                ('maphtml', models.TextField(null=True, blank=True)),
                ('directions', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
            bases=(models.Model,),
        ),
    ]
