# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nameFile', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('dateLoad', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codeInstitution', models.CharField(unique=True, max_length=20)),
                ('nameInstitution', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
                ('state', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yearWork', models.CharField(max_length=4)),
                ('state', models.BooleanField()),
                ('institucion', models.ForeignKey(to='informes.Institution')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='files',
            name='institution',
            field=models.ForeignKey(to='informes.Institution'),
        ),
    ]
