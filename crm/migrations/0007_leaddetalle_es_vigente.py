# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_auto_20170523_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaddetalle',
            name='es_vigente',
            field=models.BooleanField(default=True),
        ),
    ]
