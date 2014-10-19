# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_location_ssipevent_ssipoccurrence'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ssipevent',
            old_name='organizer',
            new_name='details',
        ),
    ]
