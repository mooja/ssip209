# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemberNewsEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(max_length=200, editable=False, unique=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('is_published', models.BooleanField(default=False, verbose_name='published')),
                ('text', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Member Submitted News Entries',
                'ordering': ['-pub_date'],
            },
            bases=(models.Model,),
        ),
    ]
