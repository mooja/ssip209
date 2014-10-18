# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20141016_0627'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ssipoccurrence',
            options={'verbose_name_plural': 'Actual Occurrences', 'verbose_name': 'Actual Occurrence'},
        ),
    ]
