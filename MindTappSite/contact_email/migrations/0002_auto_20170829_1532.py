# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 22:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_email', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recepient',
            new_name='Recipient',
        ),
    ]
