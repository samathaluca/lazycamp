from django.conf import settings
from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class campme(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    LateArrival = models.BooleanField(default=True)
    # enquiry = models.DateTimeField(default=datetime.now, blank=True)
    extras = models.IntegerField()
    setup4U = models.IntegerField(default=0)
    title = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=200, default='')
    town = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    county = models.CharField(max_length=100, default='')
    postcode = models.CharField(max_length=20, default='')
    description = models.TextField(blank=True)
    price = models.IntegerField()
    # is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name