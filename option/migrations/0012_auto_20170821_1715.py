# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 09:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('option', '0011_spot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spot',
            old_name='code',
            new_name='price',
        ),
    ]
