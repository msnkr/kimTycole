from django.db import models


# Create your models here.
class RequestContact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    number = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name