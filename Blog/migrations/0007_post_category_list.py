# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 10:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_auto_20160825_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category_list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Blog.category'),
        ),
    ]
