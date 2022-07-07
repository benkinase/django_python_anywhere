# Generated by Django 3.1.7 on 2021-05-28 20:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_auto_20210528_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 28, 22, 33, 36, 293459)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 29, 22, 33, 36, 293459)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_in_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 28, 22, 33, 36, 294459)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 29, 22, 33, 36, 294459)),
        ),
    ]