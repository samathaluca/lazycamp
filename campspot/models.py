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
    enquiry_date = models.DateTimeField(default=datetime.now, blank=True)
    extras_price = models.IntegerField()
    setup4U = models.IntegerField(default=0)

    def __str__(self):
        return self.name