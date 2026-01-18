from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('pricing/', views.pricing, name='pricing'),
    path('book-pickup/', views.book_pickup, name='book_pickup'),
    path('contact/', views.contact, name='contact'),
]
