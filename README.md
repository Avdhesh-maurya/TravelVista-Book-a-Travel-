# Tourism Management System

A Django-based web application for managing tourism destinations, bookings, and user interactions.

## Features

- **Destination Management**: Browse and manage tourism destinations
- **Hotel Management**: View and book hotels at various destinations
- **Airport Information**: Store and manage airport data
- **Travel Buddy System**: Connect with other travelers
- **Admin Dashboard**: Comprehensive admin interface for system management
- **Contact Management**: Handle user inquiries and support tickets
- **Saved Destinations**: Users can save their favorite destinations
- **User Authentication**: Secure user registration and login

## Tech Stack

- **Backend**: Django 5.2.4
- **Database**: SQLite (development), can be configured for PostgreSQL/MySQL
- **Frontend**: HTML5, CSS3, JavaScript
- **Image Processing**: Pillow
- **ORM**: Django ORM

## Project Structure

```
tourism_management/
├── adminzone/              # Admin application
│   ├── models.py          # Admin-related models
│   ├── views.py           # Admin views
│   ├── urls.py            # Admin routes
│   └── templates/         # Admin templates
├── main/                   # Main application
│   ├── models.py          # Main models (Destination, Hotel, Booking, etc.)
│   ├── views.py           # Main views
│   ├── urls.py            # Main routes
│   ├── static/            # CSS, JS, images
│   └── templates/         # Frontend templates
├── tourism_project/        # Project settings
│   ├── settings.py        # Django settings
│   ├── urls.py            # Project URL configuration
│   └── wsgi.py            # WSGI configuration
├── media/                  # User-uploaded media files
├── static/                 # Static files (CSS, JS)
├── manage.py              # Django management script
└── db.sqlite3             # Development database
```

## Installation

### Prerequisites
- Python 3.11+
- pip

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd tourism_management
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create environment configuration**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run migrations**
   ```bash
   cd tourism_management
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Load initial data (optional)**
   ```bash
   python manage.py seed_airports
   python manage.py seed_hotels
   python manage.py seed_buddies
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000/`

## Admin Access

- Navigate to `http://127.0.0.1:8000/admin/` to access the admin dashboard
- Log in with your superuser credentials

## Database Models

### Main App
- **Destination**: Tourism destinations with details, pricing, and categories
- **Hotel**: Hotel information and facilities
- **HotelBooking**: Hotel booking records
- **Booking**: Tour/destination bookings
- **SavedDestination**: User's saved favorite destinations
- **Airport**: Airport information
- **TravelBuddy**: Travel buddy connections

### Admin App
- **ContactMessage**: Contact form submissions
- **SupportTicket**: Support requests
- **User**: Extended user management

## Environment Variables

See `.env.example` for required environment variables:
- `DEBUG`: Development mode flag
- `SECRET_KEY`: Django secret key
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

## Development

### Running Tests
```bash
python manage.py test
```

### Code Style
- Follow PEP 8
- Use type hints where applicable

## Deployment

For production deployment:
1. Set `DEBUG = False` in settings
2. Use a production-grade database (PostgreSQL recommended)
3. Use a production WSGI server (Gunicorn, uWSGI)
4. Configure proper static/media file handling
5. Set up proper logging and monitoring
6. Use environment-specific settings

## License

[Specify your license here]

## Contact

[Your contact information]
