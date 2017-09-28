# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-27 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginVacation', '0003_auto_20170926_0513'),
    ]

    operations = [
        migrations.AddField(
            model_name='authemployee',
            name='department',
            field=models.CharField(choices=[('nw', 'IDC_Network'), ('sr', 'IDC_Technology')], default='nw', max_length=2),
        ),
    ]
