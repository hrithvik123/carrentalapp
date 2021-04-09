# Generated by Django 3.2 on 2021-04-09 18:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Customer'},
        ),
        migrations.AlterModelOptions(
            name='manager',
            options={'verbose_name': 'Manager'},
        ),
        migrations.AlterModelOptions(
            name='sales_associate',
            options={'verbose_name': 'Sales Associate'},
        ),
        migrations.AddField(
            model_name='vehicle',
            name='engine_no',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 18, 0, 33, 537637)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 10, 18, 0, 33, 537617)),
        ),
        migrations.AlterField(
            model_name='customer_testdrive',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 9, 18, 5, 33, 539976)),
        ),
    ]
