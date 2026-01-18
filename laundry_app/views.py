from django.shortcuts import render
from django.contrib import messages
import urllib.parse

# Create your views here.
from django.shortcuts import render, redirect
from .models import Service, PickupRequest

def home(request):
    return render(request, 'home.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def pricing(request):
    return render(request, 'pricing.html')


def book_pickup(request):
    if request.method == 'POST':
        PickupRequest.objects.create(
            name=request.POST['name'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            service=request.POST['service'],
            pickup_date=request.POST['pickup_date'],
            notes=request.POST.get('notes', ''),
        )

        # ✅ SUCCESS MESSAGE
        messages.success(
            request,
            "✅ Pickup booked successfully! Our team will contact you shortly."
        )

        return redirect('book_pickup')  # stay on same page

    return render(request, 'pickup.html')


def contact(request):
    return render(request, 'contact.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import PickupRequest
import urllib.parse

OWNER_WHATSAPP = "918530818250"  # change if needed

def book_pickup(request):
    if request.method == 'POST':
        pickup = PickupRequest.objects.create(
            name=request.POST['name'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            service=request.POST['service'],
            pickup_date=request.POST['pickup_date'],
            notes=request.POST.get('notes', ''),
        )

        # WhatsApp message content
        message = f"""
New Pickup Request 🚚

Name: {pickup.name}
Phone: {pickup.phone}
Service: {pickup.service}
Pickup Date: {pickup.pickup_date}

Address:
{pickup.address}
"""

        encoded_message = urllib.parse.quote(message)

        whatsapp_url = f"https://wa.me/{OWNER_WHATSAPP}?text={encoded_message}"

        messages.success(
            request,
            "Pickup booked successfully! Our team will contact you shortly."
        )

        return redirect(whatsapp_url)

    return render(request, 'pickup.html')


