from django.db import models


class Destination(models.Model):
    CATEGORY_CHOICES = [
        ('Beach', 'Beach'),
        ('Mountains', 'Mountains'),
        ('Heritage', 'Heritage'),
        ('Romantic', 'Romantic'),
        ('City Break', 'City Break'),
        ('Adventure', 'Adventure'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    region = models.CharField(max_length=50)  # 'Regional' or 'Foreign'
    sub_region = models.CharField(max_length=100, blank=True, default='Primary')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Adventure')
    image = models.ImageField(upload_to='destinations/', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=5000.00)
    is_featured = models.BooleanField(default=False)
    best_time = models.CharField(max_length=200, default='Oct to Mar')
    visa_info = models.TextField(blank=True, default='Visa on Arrival available for most tourists.')
    reach_info = models.TextField(blank=True, default='Well connected by flights and trains.')

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class Booking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    guests = models.PositiveIntegerField(default=1)
    booking_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, default='Pending') # Pending, Completed, Failed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.destination.name}"

class SupportTicket(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    ]
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ticket #{self.id} - {self.subject} ({self.status})"

class SavedDestination(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'destination')

    def __str__(self):
        return f"{self.user.username} saved {self.destination.name}"

class Hotel(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='hotels')
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='hotels/', blank=True)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    stars = models.IntegerField(default=3)
    amenities = models.CharField(max_length=500, default='WiFi, AC, Breakfast, Parking')

    def __str__(self):
        return f"{self.name} ({self.destination.name})"

class HotelBooking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.hotel.name}"

class TravelBuddy(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    tags = models.CharField(max_length=200) # Comma separated
    bio = models.TextField(blank=True)
    image_url = models.URLField(blank=True, default='https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=200&auto=format&fit=crop')

    def __str__(self):
        return f"{self.name} - {self.location}"

class Airport(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    airport_type = models.CharField(max_length=100) # International, Domestic, etc.
    description = models.TextField()
    image_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.city})"
