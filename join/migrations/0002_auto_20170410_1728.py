# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='join',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
