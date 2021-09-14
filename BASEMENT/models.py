from django.db import models
from django.urls import reverse

# Heng hi database a awm ho bik an ni.
class Request(models.Model):
    hming = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    domain = models.CharField(null=True, blank=True, max_length=30)
    types = models.TextField(max_length=300)

    def __str__(self):
        return self.hming

    def get_absolute_url(self):
        return reverse('home')

class Contact(models.Model):
    email = models.EmailField(max_length=30)
    title = models.CharField(max_length=20)
    message = models.TextField(max_length=300, blank=False, null=False)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('home')

