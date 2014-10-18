# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20141016_0624'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ssipevent',
            options={'verbose_name': 'Actual Event', 'verbose_name_plural': 'Actual Events'},
        ),
        migrations.AddField(
            model_name='ssipoccurrence',
            name='information',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ssipoccurrence',
            name='organizer',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
