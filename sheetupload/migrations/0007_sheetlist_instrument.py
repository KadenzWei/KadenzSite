# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-17 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheetupload', '0006_sheetlist_ispublic'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheetlist',
            name='instrument',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
