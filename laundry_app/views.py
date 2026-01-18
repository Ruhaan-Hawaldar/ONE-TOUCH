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

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, PickupRequest
import urllib.parse

OWNER_WHATSAPP = "918530818250"

def book_pickup(request):
    services = Service.objects.all()  # ✅ THIS WAS MISSING

    if request.method == 'POST':
        pickup = PickupRequest.objects.create(
            name=request.POST['name'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            service_id=request.POST['service'],  # ✅ FK FIX
            pickup_date=request.POST['pickup_date'],
            notes=request.POST.get('notes', ''),
        )

        message = f"""
New Pickup Request 🚚

Name: {pickup.name}
Phone: {pickup.phone}
Service: {pickup.service.name}
Pickup Date: {pickup.pickup_date}

Address:
{pickup.address}
"""

        whatsapp_url = f"https://wa.me/{OWNER_WHATSAPP}?text={urllib.parse.quote(message)}"

        messages.success(
            request,
            "Pickup booked successfully! Our team will contact you shortly."
        )

        return redirect(whatsapp_url)

    return render(request, 'pickup.html', {
        'services': services  # ✅ THIS FIXES DROPDOWN
    })
