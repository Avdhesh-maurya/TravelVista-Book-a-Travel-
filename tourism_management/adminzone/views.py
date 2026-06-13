from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from adminzone.models import Destination, ContactMessage


@login_required
def admin_dashboard(request):
    return render(request, 'adminzone/dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def contact_management(request):
    contact_messages = ContactMessage.objects.order_by('-created_at')
    return render(request, 'adminzone/contact_management.html', {'contact_messages': contact_messages})


@login_required
def destination(request):
    destinations = Destination.objects.all()
    return render(request, 'adminzone/destination.html', {'destinations': destinations})


@login_required
def user_management(request):
    users = User.objects.all()
    return render(request, 'adminzone/user_management.html', {'users': users})