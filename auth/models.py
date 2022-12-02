from django.db import models

# Create your models here.
class User(models.Model):
    username = models.AutoField(primary_key=True)
    password = models.CharField(max_length=50)
    face = models.CharField(max_length=100000)
    img = models.CharField(max_length=500)