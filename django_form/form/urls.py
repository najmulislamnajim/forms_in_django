from django.urls import path
from . import views

urlpatterns = [
    path('',views.form,name='form'),
    path('/greetings',views.greetings,name='greetings'),
    path('contact_received/',views.contact_received,name='contacted'),
    path('django_form/',views.django_form,name='djangoForm'),
    
]