# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-27 23:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dating_admin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionnaire',
            old_name='categoty',
            new_name='category',
        ),
    ]