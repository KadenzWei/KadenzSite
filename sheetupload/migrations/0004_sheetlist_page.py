# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-16 03:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sheetupload', '0003_auto_20170216_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheetlist',
            name='page',
            field=models.DecimalField(blank=True, decimal_places=0, default=django.utils.timezone.now, max_digits=2),
            preserve_default=False,
        ),
    ]