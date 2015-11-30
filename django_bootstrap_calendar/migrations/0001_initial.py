# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField()),
                ('place', models.CharField(max_length=50)),
                ('css_class', models.CharField(blank=True, max_length=20, verbose_name='CSS Class', choices=[(b'', 'Normal'), (b'event-warning', 'Warning'), (b'event-info', 'Info'), (b'event-success', 'Success'), (b'event-inverse', 'Inverse'), (b'event-special', 'Special'), (b'event-important', 'Important')])),
                ('start', models.DateTimeField(verbose_name='Start Date')),
                ('end', models.DateTimeField(null=True, verbose_name='End Date', blank=True)),
            ],
        ),
    ]
