# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-23 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20190917_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]
