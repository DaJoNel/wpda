# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-09 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20161108_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='city',
            field=models.CharField(max_length=63, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='createdBy',
            field=models.CharField(max_length=63, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='number',
            field=models.CharField(max_length=63, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='street',
            field=models.CharField(max_length=63, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='updatedBy',
            field=models.CharField(max_length=63, null=True),
        ),
    ]
