from django.db import models
# from django.contrib.auth.models import User


# Create your models here.
class custom(models.Model):
    user = models.CharField(blank=True, max_length=50)
    password = models.CharField(blank=True, max_length=50)


