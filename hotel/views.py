from re import A
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import stripe
from django.conf import settings
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
stripe.api_key = settings.STRIPE_SECRET_KEY

from rest_framework.permissions import (
IsAuthenticated, AllowAny,
IsAuthenticatedOrReadOnly,
IsAdminUser,
DjangoModelPermissions)
from .models import Room, Hotel, Guest,Reservation,Booking

from .serializers import (
RoomSerializer,
HotelSerializer,
GuestSerializer,
ReservationSerializer,
CheckoutSerializer,
BookingSerializer
)


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]
    #permission_classes = (RoomCreatorWritePermission,)


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [AllowAny]


class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = [AllowAny]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated,)


# TODO
class CheckoutViewSet(viewsets.ModelViewSet):
    serializer_class = CheckoutSerializer
    permission_classes = (IsAuthenticated,)

    def patch(self, request, *args, **kwargs):
        id =request.data


class BookWithPayment(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def list(self,request):
        queryset = Booking.objects.all()
        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        serializer = BookingSerializer(data=request.data)

        if serializer.is_valid():
            stripe.api_key = settings.STRIPE_SECRET_KEY
            guest = serializer.validated_data['guest']
            guests = serializer.validated_data['no_of_guests']
            price = serializer.validated_data['charges']
            stripe_token=serializer.validated_data['stripe_token']
            #guests*no_of_days*room.price
            paid_amount =   price

            try:
                stripe.Charge.create(
                amount=int(paid_amount * 100),
                currency='USD',
                description='Charge from hotel app',
                #customer=request.user,
                source=stripe_token
            )

                serializer.save(paid_amount=paid_amount,paid=True)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception:

                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self,request,pk=None):
        queryset = Reservation.objects.get(id=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





