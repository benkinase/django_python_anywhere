from django.contrib import admin
from .models import Hotel, Guest, Room, Reservation, Image,Extras,Booking

admin.site.site_header = 'Project tilapea'

class ImageInline(admin.TabularInline):
	model = Image
	extra = 0
	max_num = 10


class ExtrasInline(admin.TabularInline):
	model = Extras
	extra = 0
	max_num = 10


class RoomAdmin(admin.ModelAdmin):
	list_display= ('room_no',"name",'hotel','room_type',
	             'price','featured','capacity','is_available',)
	list_filter=("name", "room_type",)

	inlines = [
		ImageInline,
        ExtrasInline,

	 ]
	class Meta:
		model = Room


admin.site.register(Room, RoomAdmin)


class GuestAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','phone',)
admin.site.register(Guest,GuestAdmin)


class HotelAdmin(admin.ModelAdmin):
    list_display = ('name','city','max_rooms')
admin.site.register(Hotel,HotelAdmin)


class ReservationAdmin(admin.ModelAdmin):
	list_display=('guest','room','hotel','no_of_guests',
	             'check_in_date','checkout_date','check_out',
				   "charges","paid")

	list_filter=("room", "hotel",)


class BookingAdmin(admin.ModelAdmin):
	list_display=('guest','room','hotel','no_of_guests',
	             'check_in_date','checkout_date','check_out',
				   "charges",)

	list_filter=("room", "hotel",)



admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Image)
admin.site.register(Extras)


