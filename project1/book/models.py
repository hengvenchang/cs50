from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    author = models.TextField()
    year = models.CharField(max_length=255)
