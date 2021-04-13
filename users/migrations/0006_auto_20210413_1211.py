# Generated by Django 3.2 on 2021-04-13 18:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210412_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 15, 12, 11, 47, 411207)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 14, 12, 11, 47, 411207)),
        ),
        migrations.AlterField(
            model_name='customer_testdrive',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 13, 12, 16, 47, 412204)),
        ),
    ]
