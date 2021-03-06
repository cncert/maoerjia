# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-18 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0005_auto_20190318_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vipservicefee',
            name='bathe_big_dog_price_per_day',
        ),
        migrations.RemoveField(
            model_name='vipservicefee',
            name='bathe_mid_dog_price_per_day',
        ),
        migrations.RemoveField(
            model_name='vipservicefee',
            name='bathe_small_dog_price_per_day',
        ),
        migrations.RemoveField(
            model_name='vipservicefee',
            name='good_look_small_dog_price_per_day',
        ),
        migrations.RemoveField(
            model_name='vipservicefee',
            name='good_lookshuttle_big_dog_price_per_day',
        ),
        migrations.RemoveField(
            model_name='vipservicefee',
            name='good_lookshuttle_mid_dog_price_per_day',
        ),
        migrations.RemoveField(
            model_name='vipservicefee',
            name='shuttle_big_dog_price_per_day',
        ),
        migrations.RemoveField(
            model_name='vipservicefee',
            name='shuttle_mid_dog_price_per_day',
        ),
        migrations.RemoveField(
            model_name='vipservicefee',
            name='shuttle_small_dog_price_per_day',
        ),
        migrations.AddField(
            model_name='vipservicefee',
            name='bathe_big_dog_price_per_time',
            field=models.FloatField(default='100.0', verbose_name='大型犬洗澡费用'),
        ),
        migrations.AddField(
            model_name='vipservicefee',
            name='bathe_mid_dog_price_per_time',
            field=models.FloatField(default='80.0', verbose_name='中型犬洗澡费用'),
        ),
        migrations.AddField(
            model_name='vipservicefee',
            name='bathe_small_dog_price_per_time',
            field=models.FloatField(default='40.0', verbose_name='小型犬洗澡费用'),
        ),
        migrations.AddField(
            model_name='vipservicefee',
            name='good_look_small_dog_price_per_time',
            field=models.FloatField(default='40.0', verbose_name='小型犬美容费用'),
        ),
        migrations.AddField(
            model_name='vipservicefee',
            name='good_lookshuttle_big_dog_price_per_time',
            field=models.FloatField(default='100.0', verbose_name='大型犬美容费用'),
        ),
        migrations.AddField(
            model_name='vipservicefee',
            name='good_lookshuttle_mid_dog_price_per_time',
            field=models.FloatField(default='80.0', verbose_name='中型犬美容费用'),
        ),
        migrations.AddField(
            model_name='vipservicefee',
            name='shuttle_big_dog_price_per_time',
            field=models.FloatField(default='100.0', verbose_name='大型犬接送费用'),
        ),
        migrations.AddField(
            model_name='vipservicefee',
            name='shuttle_mid_dog_price_per_time',
            field=models.FloatField(default='80.0', verbose_name='中型犬接送费用'),
        ),
        migrations.AddField(
            model_name='vipservicefee',
            name='shuttle_small_dog_price_per_time',
            field=models.FloatField(default='40.0', verbose_name='小型犬接送费用'),
        ),
    ]
