# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-13 15:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='genere',
            new_name='genre',
        ),
    ]
