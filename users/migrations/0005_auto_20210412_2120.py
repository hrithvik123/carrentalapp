# Generated by Django 3.2 on 2021-04-12 21:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210412_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 14, 21, 20, 5, 287382)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 13, 21, 20, 5, 287359)),
        ),
        migrations.AlterField(
            model_name='customer_testdrive',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 12, 21, 25, 5, 288452)),
        ),
    ]
