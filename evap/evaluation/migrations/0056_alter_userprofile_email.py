# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0055_reviewer_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='email address'),
        ),
    ]
