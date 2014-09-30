# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20140922_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsentry',
            name='text_html',
            field=models.TextField(blank=True, editable=False),
        ),
    ]
