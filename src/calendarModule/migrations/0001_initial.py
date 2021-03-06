# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-10 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeNumber', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('department', models.CharField(choices=[('nw', 'IDC_Network'), ('sr', 'IDC_Technology')], default='nw', max_length=2)),
                ('vacationDate', models.DateField()),
            ],
        ),
    ]
