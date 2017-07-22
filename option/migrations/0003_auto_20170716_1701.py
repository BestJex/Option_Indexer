# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('option', '0002_intervals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intervals',
            name='lower_bound_a',
            field=models.FloatField(null=True, verbose_name='a区间下限'),
        ),
        migrations.AlterField(
            model_name='intervals',
            name='lower_bound_b',
            field=models.FloatField(null=True, verbose_name='b区间下限'),
        ),
        migrations.AlterField(
            model_name='intervals',
            name='lower_bound_c',
            field=models.FloatField(null=True, verbose_name='c区间下限'),
        ),
        migrations.AlterField(
            model_name='intervals',
            name='upper_bound_a',
            field=models.FloatField(null=True, verbose_name='a区间上限'),
        ),
        migrations.AlterField(
            model_name='intervals',
            name='upper_bound_b',
            field=models.FloatField(null=True, verbose_name='b区间上限'),
        ),
        migrations.AlterField(
            model_name='intervals',
            name='upper_bound_c',
            field=models.FloatField(null=True, verbose_name='c区间上限'),
        ),
    ]