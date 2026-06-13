from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='adminzone/change_password.html',
        success_url='/adminzone/dashboard/'
    ), name='admin_change_password'),

    path('user-management/', views.user_management, name='user_management'),
    path('contacts/', views.contact_management, name='contact_management'),
    path('destination/', views.destination, name='admin_destination_list'),

    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='adminzone/login.html'
    ), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_view, name='admin_logout'),
]
