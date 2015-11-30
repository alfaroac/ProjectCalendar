# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_bootstrap_calendar', '0002_calendarevent_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarevent',
            name='description',
            field=models.TextField(max_length=300),
        ),
    ]
