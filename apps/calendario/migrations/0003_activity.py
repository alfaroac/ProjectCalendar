# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendario', '0002_delete_calendarevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
                ('description', models.TextField()),
                ('place', models.CharField(max_length=100)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('priority', models.CharField(blank=True, max_length=20, verbose_name='CSS Class', choices=[(b'', 'Normal'), (b'event-warning', 'Warning'), (b'event-info', 'Info'), (b'event-success', 'Success'), (b'event-inverse', 'Inverse'), (b'event-special', 'Special'), (b'event-important', 'Important')])),
                ('organizer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
