from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from adminzone.forms import ContactForm
from adminzone.models import Destination, Booking, SupportTicket, SavedDestination, Hotel, HotelBooking
from datetime import datetime

# 📩 Contact Form View
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()

            try:
                # Email to admin
                send_mail(
                    subject=f"[TravelVista] New Contact: {contact_message.subject}",
                    message=f"Name: {contact_message.name}\nEmail: {contact_message.email}\n\nMessage:\n{contact_message.message}",
                    from_email='no-reply@travelvista.com',
                    recipient_list=['admin@example.com'], 
                    fail_silently=True,
                )

                # Auto-response to user
                send_mail(
                    subject='Thank You for Contacting TravelVista!',
                    message=f"Hi {contact_message.name},\n\nThank you for reaching out. We'll get back to you shortly.\n\n- Team TravelVista",
                    from_email='no-reply@travelvista.com',
                    recipient_list=[contact_message.email],
                    fail_silently=True,
                )

            except Exception:
                # Email failed but message is saved — still redirect to success
                pass

            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})


def contact_success(request):
    return render(request, 'main/contact_success.html')


def destination_list(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    destinations = Destination.objects.all()

    if query:
        destinations = destinations.filter(Q(name__icontains=query) | Q(description__icontains=query))
    if category:
        destinations = destinations.filter(category__iexact=category)

    return render(request, 'main/destination.html', {
        'destinations': destinations,
        'query': query,
        'category': category
    })


def home(request):
    featured = Destination.objects.filter(is_featured=True)[:6]
    return render(request, 'main/home.html', {'featured': featured})


def visa_policy(request):
    destinations = Destination.objects.all()
    return render(request, 'main/visa_policy.html', {'destinations': destinations})


def how_to_reach(request):
    destinations = Destination.objects.all()
    return render(request, 'main/how_to_reach.html', {'destinations': destinations})

def by_train(request):
    return render(request, 'main/by_train.html')

def by_bus(request):
    return render(request, 'main/by_bus.html')

def by_flight(request):
    from adminzone.models import Airport
    airports = Airport.objects.all()
    return render(request, "main/by_flight.html", {'airports': airports})

# --- Unique Value Proposition Features ---

def mood_filter(request):
    """
    Renders an interactive page where users can select their 'mood'
    and get destination recommendations.
    """
    destinations = Destination.objects.all()
    return render(request, 'main/mood_filter.html', {'destinations': destinations})

def ai_planner(request):
    """
    Renders a dummy AI trip itinerary generator page.
    """
    return render(request, 'main/ai_planner.html')

def buddy_matcher(request):
    """
    Renders the social 'Travel Buddy Matcher' page.
    """
    from adminzone.models import TravelBuddy
    buddies = TravelBuddy.objects.all()
    for b in buddies:
        b.tag_list = [t.strip() for t in b.tags.split(',')]
    return render(request, 'main/buddy_matcher.html', {'buddies': buddies})

def regional(request):
    destinations = Destination.objects.filter(region__iexact='Regional')
    return render(request, 'main/regional.html', {'destinations': destinations})

def foreign(request):
    destinations = Destination.objects.filter(region__iexact='Foreign')
    return render(request, 'main/foreign.html', {'destinations': destinations})

def best_time(request):
    destinations = Destination.objects.all()
    return render(request, 'main/best_time.html', {'destinations': destinations})


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')

# 🎟️ Booking & Payment Views
@login_required
def book_destination(request, dest_id):
    destination = get_object_or_404(Destination, id=dest_id)
    if request.method == 'POST':
        guests = int(request.POST.get('guests', 1))
        date = request.POST.get('date')
        
        total_price = destination.price * guests
        
        # Create a pending booking
        booking = Booking.objects.create(
            user=request.user,
            destination=destination,
            guests=guests,
            booking_date=date,
            total_price=total_price,
            payment_status='Pending'
        )
        # Redirect to mock payment page
        return render(request, 'main/payment.html', {'booking': booking})
        
    return render(request, 'main/booking.html', {'destination': destination})

@login_required
def process_payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        # Simulate payment success
        booking.payment_status = 'Completed'
        booking.save()
        return render(request, 'main/payment_success.html', {'booking': booking})
    return redirect('home')

# --- User Dashboard & Ticketing Views ---

@login_required
def user_dashboard(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    hotel_bookings = HotelBooking.objects.filter(user=request.user).order_by('-created_at')
    saved_destinations = SavedDestination.objects.filter(user=request.user).order_by('-added_at')
    tickets = SupportTicket.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'main/dashboard.html', {
        'bookings': bookings,
        'hotel_bookings': hotel_bookings,
        'saved_destinations': saved_destinations,
        'tickets': tickets
    })

@login_required
def create_ticket(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        SupportTicket.objects.create(user=request.user, subject=subject, message=message)
        return redirect('user_dashboard')
    return render(request, 'main/create_ticket.html')

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    # Only allow cancellation if pending or confirmed (logic can be expanded)
    if booking.payment_status == 'Pending':
        booking.delete()
    else:
        booking.payment_status = 'Cancelled'
        booking.save()
    return redirect('user_dashboard')

@login_required
def save_destination(request, dest_id):
    destination = get_object_or_404(Destination, id=dest_id)
    SavedDestination.objects.get_or_create(user=request.user, destination=destination)
    return redirect('user_dashboard')

@login_required
def remove_saved(request, saved_id):
    saved = get_object_or_404(SavedDestination, id=saved_id, user=request.user)
    saved.delete()
    return redirect('user_dashboard')

# 🏨 Hotel Views
def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'main/hotels.html', {'hotels': hotels})

@login_required
def book_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    if request.method == 'POST':
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        guests = int(request.POST.get('guests', 1))
        
        # Simple days calculation
        try:
            d1 = datetime.strptime(check_in, '%Y-%m-%d')
            d2 = datetime.strptime(check_out, '%Y-%m-%d')
            nights = (d2 - d1).days
            if nights < 1: nights = 1
        except:
            nights = 1
        
        total_price = hotel.price_per_night * nights * guests
        
        booking = HotelBooking.objects.create(
            user=request.user,
            hotel=hotel,
            check_in=check_in,
            check_out=check_out,
            guests=guests,
            total_price=total_price,
            payment_status='Pending'
        )
        return render(request, 'main/hotel_payment.html', {'booking': booking})
    
    return render(request, 'main/hotel_detail.html', {'hotel': hotel})

@login_required
def process_hotel_payment(request, booking_id):
    booking = get_object_or_404(HotelBooking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.payment_status = 'Completed'
        booking.save()
        return render(request, 'main/hotel_payment_success.html', {'booking': booking})
    return redirect('user_dashboard')




