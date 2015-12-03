# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accesos',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='accesos',
            name='rol',
        ),
        migrations.DeleteModel(
            name='Accesos',
        ),
        migrations.DeleteModel(
            name='Direcion',
        ),
    ]
