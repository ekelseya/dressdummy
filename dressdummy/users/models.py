from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.username)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    about = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='media', blank=True)
