# Generated by Django 3.2 on 2021-04-13 21:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20210413_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 15, 15, 36, 27, 731941)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 14, 15, 36, 27, 731941)),
        ),
        migrations.AlterField(
            model_name='customer_testdrive',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 13, 15, 41, 27, 732938)),
        ),
    ]
