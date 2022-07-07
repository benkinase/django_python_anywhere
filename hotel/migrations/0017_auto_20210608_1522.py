# Generated by Django 3.1.7 on 2021-06-08 13:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0016_auto_20210606_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 8, 15, 22, 51, 658207)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 9, 15, 22, 51, 658207)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_in_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 8, 15, 22, 51, 659209)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 9, 15, 22, 51, 659209)),
        ),
    ]