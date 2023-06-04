from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Glizzy(models.Model):
  name = models.CharField(max_length=100)
  toppings = models.TextField(max_length=250)
  description = models.TextField(max_length=250)
  price = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)