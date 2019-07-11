from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_innovator = models.BooleanField(default=False)
    is_investor = models.BooleanField(default=False)
    is_entrepreneur = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles')
    address = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    profession = models.CharField(max_length=250)
    street = models.CharField(max_length=250, blank=True)
    town = models.CharField(max_length=250, blank=True)
    zip_code = models.IntegerField(default=00000)
    country = models.CharField(max_length=250, blank=True)
    phone_number = models.IntegerField(blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user)

