from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=500, unique=True)
	author = models.CharField(max_length=125, blank=True)
	image = models.ImageField(upload_to='books/images', blank=True)
	image_url = models.URLField(blank=True)
	descriptions = models.TextField(blank=True)
	download = models.URLField(blank=True)
	slug = models.SlugField(allow_unicode=True, unique=True, blank=True)

	class Meta:
		verbose_name = "Book"
		verbose_name_plural = "Books"
		ordering = ["title"]

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse("books:book-detail", kwargs={"slug": self.slug})
