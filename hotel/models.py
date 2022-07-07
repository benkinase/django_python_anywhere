from django.db import models
from datetime import datetime, date, timedelta
from django.utils.text import slugify
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from enum import IntEnum
from django.dispatch import receiver
from django.db.models.signals import post_save


ROOM_TYPES = (
    ('standard', _('standard')),
    ('executive', _('executive')),
    ('family', _('family')),
    ('single', _('single')),
    ('double', _('double')),

)


class ROOM_SIZES(IntEnum):
    S400 = 400
    S600 = 600
    S800 = 800
    S1000 = 1000
    S1200 = 1200
    S1400 = 1400

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Hotel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    num_rooms = models.IntegerField(default=100)
    res_buffer = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_max_rooms(self):
        return ((self.res_buffer / 100) * self.num_rooms) + self.num_rooms

    max_rooms = property(get_max_rooms)

    class Meta:
        ordering = ('name',)


class Guest(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Room(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    room_no = models.IntegerField(default=None, unique=True)
    hotel = models.ForeignKey(Hotel, null=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    size = models.IntegerField(
        choices=ROOM_SIZES.choices(), default=ROOM_SIZES.S400)
    no_of_beds = models.IntegerField(default=1)
    capacity = models.IntegerField(default=1)
    room_type = models.CharField(
        max_length=32, choices=ROOM_TYPES, default='standard')
    slug = models.SlugField(blank=True)
    price = models.FloatField(blank=True, null=True)
    promo = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    pets = models.BooleanField(default=False)
    breakfast = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def hotel_name(self):
        return self.hotel.name

    def get_room_size_label(self):
        return ROOM_SIZES(self.room_type).name.title()


def image_upload_to(instance, filename):
    name = instance.room.name
    slug = slugify(name)
    basename, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" % (slug, instance.room.id, file_extension)
    return "hotel/%s/%s" % (slug, new_filename)


class Image(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to=image_upload_to)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="images", null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Extras(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    extra = models.TextField(blank=True, null=True)
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="extras", null=True, blank=True)

    class Meta:
        verbose_name_plural = "extras"

    def __str__(self):
        return self.title


class Booking(models.Model):
    guest = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='bookings', on_delete=models.CASCADE)
    hotel = models.ForeignKey(
        Hotel, related_name="bookings", on_delete=models.CASCADE)
    room = models.ForeignKey(
        Room, related_name='bookings', on_delete=models.CASCADE)
    no_of_guests = models.IntegerField(
        choices=list(zip(range(1, 10), range(1, 10))))
    check_in_date = models.DateTimeField(default=datetime.now())
    checkout_date = models.DateTimeField(
        default=datetime.now() + timedelta(days=1))
    check_out = models.BooleanField(default=False)
    charges = models.FloatField(default=0)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    stripe_token = models.CharField(max_length=100)

    class Meta:
        ordering = ['-created_at', ]

    def __str__(self):
        return f"{self.hotel.name}"


class Reservation(models.Model):
    guest = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    hotel = models.ForeignKey(
        Hotel, related_name="reservations", on_delete=models.CASCADE)
    room = models.ForeignKey(
        Room, related_name='reservation', on_delete=models.CASCADE)
    no_of_guests = models.IntegerField(
        choices=list(zip(range(1, 10), range(1, 10))))
    check_in_date = models.DateTimeField(default=datetime.now())
    checkout_date = models.DateTimeField(
        default=datetime.now() + timedelta(days=1))
    check_out = models.BooleanField(default=False)
    charges = models.FloatField(default=0)
    paid = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f'{self.check_in_date} {self.checkout_date.strftime("%Y-%m-%d")},{self.hotel.name},{str(self.room.room_no)},{self.room.room_type},{self.guest.username}'
        )

# handle room availability toggle


@receiver(post_save, sender=Reservation)
def handle_booking(instance, created, **kwargs):
    room = instance.room
    if created:
        room.is_available = False
        room.save()
    if instance.check_out == True:
        room.is_available = True
        room.save()
