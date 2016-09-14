# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_add_indexes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_value',
            field=models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Document value'),
        ),
        migrations.AlterField(
            model_name='document',
            name='net_value',
            field=models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Net value'),
        ),
        migrations.AlterField(
            model_name='document',
            name='reimbursement_value',
            field=models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Reimbusrsement value'),
        ),
        migrations.AlterField(
            model_name='document',
            name='remark_value',
            field=models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Remark value'),
        ),
    ]
