# Generated by Django 3.2 on 2021-04-13 20:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210413_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 15, 14, 26, 18, 905701)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 14, 14, 26, 18, 905701)),
        ),
        migrations.AlterField(
            model_name='customer_testdrive',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 13, 14, 31, 18, 906698)),
        ),
    ]
