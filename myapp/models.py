from django.db import models

# Create your models here.
class registertable(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
