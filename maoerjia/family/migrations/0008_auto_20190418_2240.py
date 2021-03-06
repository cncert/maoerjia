# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-18 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0007_auto_20190318_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vipservicefee',
            name='bathe_big_dog_price_per_time',
            field=models.FloatField(default='100.0', verbose_name='洗澡费(大)'),
        ),
        migrations.AlterField(
            model_name='vipservicefee',
            name='bathe_mid_dog_price_per_time',
            field=models.FloatField(default='80.0', verbose_name='洗澡费(中)'),
        ),
        migrations.AlterField(
            model_name='vipservicefee',
            name='bathe_small_dog_price_per_time',
            field=models.FloatField(default='40.0', verbose_name='洗澡费(小)'),
        ),
        migrations.AlterField(
            model_name='vipservicefee',
            name='good_look_small_dog_price_per_time',
            field=models.FloatField(default='40.0', verbose_name='美容费(小)'),
        ),
        migrations.AlterField(
            model_name='vipservicefee',
            name='good_lookshuttle_big_dog_price_per_time',
            field=models.FloatField(default='100.0', verbose_name='美容费(大)'),
        ),
        migrations.AlterField(
            model_name='vipservicefee',
            name='good_lookshuttle_mid_dog_price_per_time',
            field=models.FloatField(default='80.0', verbose_name='美容费(中)'),
        ),
        migrations.AlterField(
            model_name='vipservicefee',
            name='shuttle_big_dog_price_per_time',
            field=models.FloatField(default='100.0', verbose_name='接送费(大)'),
        ),
        migrations.AlterField(
            model_name='vipservicefee',
            name='shuttle_mid_dog_price_per_time',
            field=models.FloatField(default='80.0', verbose_name='接送费(中)'),
        ),
        migrations.AlterField(
            model_name='vipservicefee',
            name='shuttle_small_dog_price_per_time',
            field=models.FloatField(default='40.0', verbose_name='接送费(小)'),
        ),
    ]
