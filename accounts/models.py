from typing import Any

from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from cloudinary.models import CloudinaryField

User = get_user_model()


class UserProfile(models.Model):
    class GenderChoices(models.TextChoices):
        male = 'm', 'Male'
        female = 'f', 'Female'
        other = 'o', 'Other'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = CloudinaryField('Profile Avatar', null=True, blank=True)

    gender = models.CharField(max_length=1, choices=GenderChoices.choices, null=True, blank=True)

    dob = models.DateField(blank=True, null=True)
    number_prefix = models.CharField(max_length=10, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)

    address = models.CharField(max_length=255, null=True, blank=True)
    suburb = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.PositiveSmallIntegerField(null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    province = models.CharField(max_length=255, null=True, blank=True)
    preferred_language = models.CharField(max_length=50, choices=settings.LANGUAGES, default='en')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


@receiver(post_save, sender=User)
def save_user_profile(sender: Any, instance: User, **kwargs: Any) -> None:
    userprofile, created = UserProfile.objects.get_or_create(user=instance)
    userprofile.save()
