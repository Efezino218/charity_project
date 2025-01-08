# holdingcore_app/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  # Placeholder for homepage
    path('about/', views.about, name='about'),
    path('causes/', views.causes, name='causes'),
    path('programs/', views.programs, name='programs'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('blog/', views.blog, name='blog'),
    path('event_gallery/', views.event_gallery, name='event_gallery'),
    path('guidelines/', views.guidelines, name='guidelines'),
    path('donate/', views.donate, name='donate'),
    path('contact/', views.contact, name='contact'),
    # path('donate/', views.donate, name='donate'),
    # path('donation-form/', views.initialize_payment, name='donation_form'),  # Show form and handle POST
    path('initialize-payment/', views.initialize_payment, name='initialize_payment'),  # Handle initialization
    path('verify-payment/', views.verify_payment, name='verify_payment'),  # Verify payment 

]