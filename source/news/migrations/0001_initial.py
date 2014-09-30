# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, unique=True, max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('is_published', models.BooleanField(verbose_name='published', default=False)),
                ('text', models.TextField(blank=True)),
                ('text_html', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
            bases=(models.Model,),
        ),
    ]
