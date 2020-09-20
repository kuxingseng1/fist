from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class 普通会员表(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(blank=True, max_length=50)
    birth = models.DateField(blank=True)

    class Meta:
        verbose_name_plural = "普通会员表"
