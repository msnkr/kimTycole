from django.db import models
from django.utils import timezone


# Create your models here.
class RequestContact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    number = models.CharField(max_length=20, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name

class OurWork(models.Model):
    number = models.CharField(max_length=3, default=None)
    date = models.DateTimeField(default=timezone.now)
    img = models.ImageField()

    def __str__(self):
        return self.number