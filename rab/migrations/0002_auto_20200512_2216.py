# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-12 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rab',
            name='proposal',
            field=models.CharField(max_length=100),
        ),
    ]