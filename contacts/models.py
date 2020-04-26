from django.db import models
from datetime import datetime
from campspot.models import campspot

# Create your models here.


    # photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')

class contact(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    contact = models.ForeignKey(campspot, on_delete=models.DO_NOTHING)

def __str__(self):
        return self.name