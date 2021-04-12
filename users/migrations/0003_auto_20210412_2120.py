# Generated by Django 3.2 on 2021-04-12 21:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210412_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_service',
            name='bot_chat',
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 14, 21, 20, 0, 98992)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 13, 21, 20, 0, 98967)),
        ),
        migrations.AlterField(
            model_name='customer_testdrive',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 12, 21, 25, 0, 100099)),
        ),
    ]
