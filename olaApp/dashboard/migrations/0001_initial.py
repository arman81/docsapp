# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0001_initial'),
        ('driverapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('start_time', models.DateTimeField(null=True, auto_now_add=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('status', models.CharField(max_length=50, blank=True, choices=[('wating', 'wating'), ('ongoing', 'ongoing'), ('completed', 'completed')])),
                ('active', models.BooleanField(default=True)),
                ('customer', models.ForeignKey(blank=True, null=True, default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='customerapp.Customer')),
                ('driver', models.ForeignKey(blank=True, null=True, default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='driverapp.Driver')),
            ],
        ),
    ]
