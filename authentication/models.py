from django.contrib import(admin)
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.TextField()
    face = models.TextField()
    img = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.username

admin.site.register(User)