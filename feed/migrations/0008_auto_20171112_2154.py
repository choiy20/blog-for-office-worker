# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-12 13:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_comment_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='commenting',
        ),
    ]
