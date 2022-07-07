# Generated by Django 3.1.7 on 2021-05-28 20:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_auto_20210528_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 28, 22, 36, 7, 336307)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 29, 22, 36, 7, 336307)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_in_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 28, 22, 36, 7, 336307)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 29, 22, 36, 7, 336307)),
        ),
    ]