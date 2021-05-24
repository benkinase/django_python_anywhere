from rest_framework import serializers
import datetime
from .models import Booking, Room, Hotel,Guest,Reservation,Image, Extras


class ImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Image
    fields = ('__all__')


class ExtraSerializer(serializers.ModelSerializer):
  class Meta:
    model = Extras
    fields = ('__all__')


class RoomSerializer(serializers.ModelSerializer):
  hotel = serializers.ReadOnlyField(source='hotel.id')
  images= ImageSerializer(many=True, read_only=True)
  extras= ExtraSerializer(many=True, read_only=True)

  class Meta:
    model = Room
    fields=("__all__")


class HotelSerializer(serializers.ModelSerializer):
  max_rooms=serializers.IntegerField(read_only=True)
  rooms= RoomSerializer(many=True, read_only=True)

  class Meta:
    model = Hotel
    fields = ('id','name',"city","rooms",)

  # def get_max(self,model):
  #   return  get_max_rooms()


class GuestSerializer(serializers.ModelSerializer):
  class Meta:
    model = Guest
    fields = '__all__'


# Current
class ReservationSerializer(serializers.ModelSerializer):

  class Meta:
    model = Reservation
    fields =('id','guest','no_of_guests', 'room','hotel','check_in_date',
              'checkout_date','charges','paid',
            )


#:: Implement guest checkout
class CheckoutSerializer(serializers.ModelSerializer):

  class Meta:
    model = Reservation
    fields =('id',"guest","hotel","no_of_guests",'room',)


# :: Resolve Bad Request error and implement stripe payment
class BookingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Booking
    fields=('id','guest','no_of_guests','room','hotel','check_in_date',
              'checkout_date','charges','stripe_token',
            )

  def create(self, data):
    print(data)
    reservation = Booking.objects.create(**data)
    return reservation


  # object level validation
  def validate(self, data):
    if not data['checkout_date']:
      raise serializers.ValidationError("Checkout must occur after checkin")
    return data

  # custom field validation
  # def validate_guest(self,value):
  #   if not value:
  #     raise serializers.ValidationError('Guest must be at least 1')
  #   return value

  def validate_no_of_guests(self,value):
    if not value > 0:
      raise serializers.ValidationError('Guest must be at least 1')
    return value

  def validate_room(self,value):
    if not value:
      raise serializers.ValidationError('A room must be selected')
    return value

  def validate_stripe_token(self,value):
    if not value:
      raise serializers.ValidationError('Payment token is missing')
    return value
