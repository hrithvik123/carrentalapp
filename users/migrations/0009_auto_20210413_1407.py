# Generated by Django 3.2 on 2021-04-13 20:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210413_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='owner',
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 15, 14, 7, 2, 146384)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 14, 14, 7, 2, 146384)),
        ),
        migrations.AlterField(
            model_name='customer_testdrive',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 13, 14, 12, 2, 147382)),
        ),
    ]
