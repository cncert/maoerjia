# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-04 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import family.models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0002_auto_20190304_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homephoto',
            name='photo_name',
            field=models.CharField(blank=True, default=family.models.HomePhoto.default_photo_name, max_length=512, null=True, verbose_name='照片名称'),
        ),
    ]