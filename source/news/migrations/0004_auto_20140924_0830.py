# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20140922_1515'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsentry',
            options={'ordering': ['-pub_date'], 'verbose_name_plural': 'News Entries'},
        ),
    ]
