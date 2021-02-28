from django.db import models
from django.utils import timezone


class Target(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    expiration_date = models.DateField(null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
