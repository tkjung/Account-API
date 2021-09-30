from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

DEPT_CHOICES = {
    ('mju', 'MJU'),
    ('uplex', 'UPLEX'),
    ('not-specified', 'Not Specified')
}

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    dept = models.CharField(max_length=100, choices=DEPT_CHOICES, null=True)
    email = models.EmailField(max_length=50)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
    zonecode = models.CharField(max_length=100, default=0)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()