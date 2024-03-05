from django.urls import path
from .views import *

urlpatterns = [
    path('',Home, name='home'),
    path('product',Products, name='products'),
    path('tracking',TrackingPage, name='tracking'),
    path('learnmore',Learnmore, name='learn-more'),
    path('contact',Contact, name='contact'),
    path('ask',Ask, name='ask'),
    path('addtrack',addTracks, name='addtrack'),
    path('edit/<tracks_id>',edit, name='edit'),
    path('delete/<tracks_id>',delete,name='delete'),
]