# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-27 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarModule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(choices=[('nw', 'IDC_Network'), ('sr', 'IDC_Technology')], default='nw', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employeeNumber',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='vacationDate',
            field=models.DateField(null=True),
        ),
    ]
