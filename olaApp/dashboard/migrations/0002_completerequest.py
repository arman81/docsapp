# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driverapp', '0001_initial'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompleteRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('driver', models.ForeignKey(blank=True, null=True, default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='driverapp.Driver')),
                ('request', models.ForeignKey(blank=True, null=True, default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='dashboard.Request')),
            ],
        ),
    ]
