# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('informes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yearWork', models.CharField(max_length=4)),
                ('state', models.BooleanField()),
                ('institution', models.OneToOneField(to='informes.Institution')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Informes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nameFile', models.CharField(max_length=100)),
                ('fileInform', models.FileField(upload_to=b'informes')),
                ('description', models.TextField()),
                ('dateLoad', models.DateTimeField(auto_now_add=True)),
                ('institution', models.ForeignKey(to='informes.Institution')),
            ],
        ),
        migrations.RemoveField(
            model_name='files',
            name='institution',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='institucion',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='user',
        ),
        migrations.DeleteModel(
            name='Files',
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
    ]
