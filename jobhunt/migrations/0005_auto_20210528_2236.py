# Generated by Django 3.1.7 on 2021-05-28 20:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobhunt', '0004_auto_20210528_2233'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='JobApplication',
            new_name='Application',
        ),
        migrations.AlterField(
            model_name='interview',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 28, 22, 36, 7, 338306)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 28, 22, 36, 7, 339308)),
        ),
    ]