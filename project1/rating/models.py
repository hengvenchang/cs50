from django.db import models

# Create your models here.
class Rating(models.Model):
    book_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    length = models.BigIntegerField()
