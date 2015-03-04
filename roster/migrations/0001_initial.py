# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('instructor', models.CharField(max_length=50)),
                ('description', models.CharField(default=b'', max_length=200)),
                ('term', models.CharField(max_length=50)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-date', 'name'),
                'verbose_name_plural': 'Courses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('pid', models.CharField(unique=True, max_length=12)),
                ('grade', models.IntegerField(max_length=3)),
            ],
            options={
                'ordering': ('pid', 'name'),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='roster.Student'),
            preserve_default=True,
        ),
    ]
