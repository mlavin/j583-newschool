# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='callnumber',
            field=models.CharField(max_length=4, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.IntegerField(max_length=3, null=True),
            preserve_default=True,
        ),
    ]
