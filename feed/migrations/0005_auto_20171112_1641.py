# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-12 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_auto_20171112_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Heading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=500)),
            ],
        ),
        migrations.RenameModel(
            old_name='Subtitle',
            new_name='Subeading',
        ),
        migrations.RenameField(
            model_name='subeading',
            old_name='subtitle',
            new_name='subheading',
        ),
    ]