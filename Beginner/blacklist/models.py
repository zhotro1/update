from django.db import models

# Create your models here.

class Blacklist(models.Model):
	ip_addr = models.GenericIPAddressField()

	def __str__(self):
		return self.ip_addr
