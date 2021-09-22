from django.db import models
from django_cryptography.fields import encrypt

class Totp(models.Model):
    userId = models.IntegerField()
    secret = encrypt(models.CharField(max_length=32))
