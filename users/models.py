from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    about = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='media', blank=True)
