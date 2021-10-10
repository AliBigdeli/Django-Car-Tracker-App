from django.db import models
from django.contrib.auth.models import User
from .utils import create_device_token

class Device(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=255)
    token = models.CharField(max_length=15, unique=True, blank=True)
    cellnumber = models.CharField(max_length=12,null=True)
    descriptions = models.TextField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_date"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        # If the short url wasn't specified
        if not self.token:
            # We pass the model instance that is being saved
            self.token = create_device_token(self)

        super().save(*args, **kwargs)

class Coordinate(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    z = models.FloatField(null=True,blank=True)
    #time = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.device.name
    
    class Meta:
        ordering = ["-created_date"]

    