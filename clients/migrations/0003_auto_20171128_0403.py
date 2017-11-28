# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-28 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_ticketmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketmodel',
            name='ticket_type',
            field=models.CharField(choices=[('Bug Report', 'Bug Report'), ('Feature Request', 'Feature Request'), ('Other', 'Other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ticketmodel',
            name='urgency',
            field=models.CharField(choices=[('Low', 'Low'), ('Mid', 'Mid'), ('High', 'High')], max_length=50),
        ),
    ]