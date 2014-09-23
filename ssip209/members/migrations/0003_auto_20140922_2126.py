# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20140922_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.CharField(null=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='member',
            name='canhelp',
            field=models.CharField(null=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='member',
            name='cellphone',
            field=models.CharField(null=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='member',
            name='hobbies',
            field=models.CharField(null=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='member',
            name='homephone',
            field=models.CharField(null=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='needhelp',
            field=models.CharField(null=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='member',
            name='town',
            field=models.CharField(null=True, max_length=200),
        ),
    ]
