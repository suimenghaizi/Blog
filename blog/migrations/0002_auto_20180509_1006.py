# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-05-09 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date_publish']},
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.CharField(max_length=500),
        ),
    ]
