from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def creat_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)
