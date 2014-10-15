# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('status', model_utils.fields.StatusField(no_check_for_status=True, choices=[('draft', 'draft'), ('published', 'published')], max_length=20, default='draft')),
                ('text_format', model_utils.fields.StatusField(no_check_for_status=True, choices=[('draft', 'draft'), ('published', 'published')], max_length=100, default='raw')),
                ('title', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, max_length=200, editable=False)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Pages',
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
    ]
