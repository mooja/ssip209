# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20141017_1405'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name_plural': 'Locations', 'verbose_name': 'Location'},
        ),
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.CharField(max_length=400, null=True),
            preserve_default=True,
        ),
    ]
