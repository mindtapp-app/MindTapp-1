# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_email', '0002_auto_20170829_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipient',
            name='email',
            field=models.EmailField(help_text='Upon hitting contact me on the main page, will send an email to all emails listed here.', max_length=254),
        ),
    ]
