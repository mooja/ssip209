# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('birthday', models.DateField()),
                ('town', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=400)),
                ('email', models.EmailField(max_length=200)),
                ('homephone', models.CharField(max_length=20)),
                ('cellphone', models.CharField(max_length=20)),
                ('hobbies', models.CharField(max_length=500)),
                ('canhelp', models.CharField(max_length=500)),
                ('needhelp', models.CharField(max_length=500)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, max_length=200, editable=False)),
                ('c_date', models.DateTimeField(verbose_name='date added', auto_now_add=True)),
            ],
            options={
                'ordering': ['last_name'],
            },
            bases=(models.Model,),
        ),
    ]
