from django.db import models

# Create your models here.
class Persion(models.Model):
	persion_img = models.ImageField(upload_to='persions/images')
	persion_name = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.persion_name
