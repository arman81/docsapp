# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('customer_id', models.CharField(max_length=200, unique=True, db_index=True)),
                ('name', models.CharField(max_length=200, blank=True, null=True)),
                ('email', models.CharField(max_length=100, blank=True, null=True)),
            ],
        ),
    ]
