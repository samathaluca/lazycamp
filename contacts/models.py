from django.db import models
from datetime import datetime

class Contact(models.Model):
  campspot = models.CharField(max_length=200, default='')
  campspot_id = models.IntegerField(default='1')
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100, default='')
  phone = models.CharField(max_length=100, default='')
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  user_id = models.IntegerField(default='', blank=True)
  def __str__(self):
    return self.name
    
