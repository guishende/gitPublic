# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20161022_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='createddate',
            field=models.DateField(blank=True, db_column='createdDate', default=b'2016-10-23', null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='news',
            name='createddate',
            field=models.DateField(blank=True, db_column='createdDate', default=b'2016-10-23', null=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='products',
            name='createddate',
            field=models.DateField(blank=True, db_column='createdDate', default=b'2016-10-23', verbose_name='Created Date'),
        ),
    ]