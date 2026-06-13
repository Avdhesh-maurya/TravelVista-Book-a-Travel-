from django.urls import path
from . import views

urlpatterns = [
    # Homepage
    path('', views.home, name='home'),

    # Contact page with form submission
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),

    # Visa policy page
    path('visa-policy/', views.visa_policy, name='visa_policy'),

    # How to Reach section
    path('how-to-reach/', views.how_to_reach, name='how_to_reach'),
    path('how-to-reach/train/', views.by_train, name='by_train'),
    path('how-to-reach/bus/', views.by_bus, name='by_bus'),
    path('how-to-reach/flight/', views.by_flight, name='by_flight'),

    # Destination section
    path('destination/', views.destination_list, name='destination'),

    path('destination/regional/', views.regional, name='regional'),
    path('destination/foreign/', views.foreign, name='foreign'),
    path('destinations/', views.destination_list, name='destination_list'),

    # Best time to visit page
    path('best-time/', views.best_time, name='best_time'),

    # Auth routes
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),

    # Booking & Payment
    path('book/<int:dest_id>/', views.book_destination, name='book_destination'),
    path('payment/<int:booking_id>/', views.process_payment, name='process_payment'),

    # Unique Features
    path('mood/', views.mood_filter, name='mood_filter'),
    path('ai-planner/', views.ai_planner, name='ai_planner'),
    path('buddy-matcher/', views.buddy_matcher, name='buddy_matcher'),

    # User Dashboard & Ticketing
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('dashboard/cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('dashboard/save-destination/<int:dest_id>/', views.save_destination, name='save_destination'),
    path('dashboard/remove-saved/<int:saved_id>/', views.remove_saved, name='remove_saved'),
    path('dashboard/tickets/create/', views.create_ticket, name='create_ticket'),

    # Hotel Booking System
    path('hotels/', views.hotel_list, name='hotel_list'),
    path('hotels/book/<int:hotel_id>/', views.book_hotel, name='book_hotel'),
    path('hotels/payment/<int:booking_id>/', views.process_hotel_payment, name='process_hotel_payment'),
]
