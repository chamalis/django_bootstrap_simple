# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='creation_date',
        ),
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(default='Hello', max_length=200),
            preserve_default=False,
        ),
    ]
