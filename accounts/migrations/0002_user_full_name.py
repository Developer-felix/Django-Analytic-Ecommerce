# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-10 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
