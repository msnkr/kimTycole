from django.db import models
from django.utils import timezone
from PIL import Image


# Create your models here.
class RequestContact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    number = models.CharField(max_length=20, blank=True)
    message = models.TextField()


    def __str__(self):
        return self.name


class OurWork(models.Model):
    name = models.CharField(max_length=15, default=None)
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField()


    # def save_file(self):
    #     super().save()
    #     img = Image.open(self.image.path)
    #     img.save(self.image.path, optimize=True, quality=35)


    def __str__(self):
        return self.name
