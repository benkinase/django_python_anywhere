from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('api/rooms', views.RoomViewSet, "rooms"),
router.register('api/hotels', views.HotelViewSet, "hotels"),
router.register('api/guests', views.GuestViewSet, "guests"),
router.register('api/pay/stripe', views.BookWithPayment,"reserve"),
router.register('api/booking', views.BookingViewSet, "booking"),
router.register('api/check-out', views.CheckoutViewSet, "checkout"),


urlpatterns = router.urls
