# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(verbose_name=b'date registered')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
