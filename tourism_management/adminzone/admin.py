from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Destination, ContactMessage, Hotel, HotelBooking


@admin.action(description='Mark selected destinations as Featured')
def make_featured(modeladmin, request, queryset):
    queryset.update(region='Featured')

@admin.action(description='Unmark selected destinations as Featured')
def unmake_featured(modeladmin, request, queryset):
    queryset.update(region='')


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'region')
    actions = [make_featured, unmake_featured]
    search_fields = ('name', 'region')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)


admin.site.site_header = format_html(
    '<a href="{}" style="color: white; text-decoration: none;">TravelVista Admin Dashboard</a>',
    reverse('admin_dashboard')  # Make sure this name is defined in your `urls.py`
)
admin.site.site_title = "TravelVista Admin"
admin.site.index_title = "Site Administration"


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination', 'price_per_night', 'stars')
    list_filter = ('destination', 'stars')
    search_fields = ('name', 'destination__name')


@admin.register(HotelBooking)
class HotelBookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'hotel', 'check_in', 'check_out', 'payment_status', 'total_price')
    list_filter = ('payment_status', 'check_in')


