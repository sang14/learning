# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0003_join_ip_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
