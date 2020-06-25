from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
# Create your models here.

class student(models.Model):
    std_name = models.CharField(max_length=50)
    std_rollno = models.CharField(max_length=10)
    std_id = models.IntegerField()

    def __str__(self):
        return self.std_name


class profile(models.Model):
    name = models.CharField(max_length=50)
    pic = models.ImageField(upload_to='profiles', blank=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)