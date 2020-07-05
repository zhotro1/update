from django.db import models

# Create your models here.

class EnglishAppModel(models.Model):
	card_name = models.CharField(max_length=100, unique=True, blank=False)
	card_pic = models.ImageField(null=False, blank=False)
	card_voice = models.FileField(null=False, blank=False)

	def __str__(self):
		return self.card_name
