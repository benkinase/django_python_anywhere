# Generated by Django 4.0.3 on 2022-07-07 12:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hotel.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('num_rooms', models.IntegerField(default=100)),
                ('res_buffer', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('room_no', models.IntegerField(default=None, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('size', models.IntegerField(choices=[(400, 'S400'), (600, 'S600'), (800, 'S800'), (1000, 'S1000'), (1200, 'S1200'), (1400, 'S1400')], default=hotel.models.ROOM_SIZES['S400'])),
                ('no_of_beds', models.IntegerField(default=1)),
                ('capacity', models.IntegerField(default=1)),
                ('room_type', models.CharField(choices=[('standard', 'standard'), ('executive', 'executive'), ('family', 'family'), ('single', 'single'), ('double', 'double')], default='standard', max_length=32)),
                ('slug', models.SlugField(blank=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('promo', models.BooleanField(default=False)),
                ('is_available', models.BooleanField(default=True)),
                ('pets', models.BooleanField(default=False)),
                ('breakfast', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=False)),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_guests', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('check_in_date', models.DateTimeField(default=datetime.datetime(2022, 7, 7, 14, 2, 2, 844954))),
                ('checkout_date', models.DateTimeField(default=datetime.datetime(2022, 7, 8, 14, 2, 2, 844954))),
                ('check_out', models.BooleanField(default=False)),
                ('charges', models.FloatField(default=0)),
                ('paid', models.BooleanField(default=False)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='hotel.hotel')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='hotel.room')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to=hotel.models.image_upload_to)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='hotel.room')),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Extras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('extra', models.TextField(blank=True, null=True)),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='extras', to='hotel.room')),
            ],
            options={
                'verbose_name_plural': 'extras',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_guests', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('check_in_date', models.DateTimeField(default=datetime.datetime(2022, 7, 7, 14, 2, 2, 844954))),
                ('checkout_date', models.DateTimeField(default=datetime.datetime(2022, 7, 8, 14, 2, 2, 844954))),
                ('check_out', models.BooleanField(default=False)),
                ('charges', models.FloatField(default=0)),
                ('paid', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('paid_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('stripe_token', models.CharField(max_length=100)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='hotel.hotel')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='hotel.room')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
