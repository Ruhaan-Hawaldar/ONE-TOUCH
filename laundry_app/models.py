from django.db import models

# Create your models here.
from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class PickupRequest(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('picked', 'Picked'),
        ('billed', 'Billed'),
        ('delivered', 'Delivered'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    service = models.CharField(max_length=100)
    pickup_date = models.DateField()
    notes = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.status.capitalize()}"

