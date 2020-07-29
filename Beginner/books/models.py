from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.core.exceptions import ValidationError


# Create your models here.

class Book(models.Model):
	def validate_image(fieldfile_obj):
		filesize = fieldfile_obj.file.size
		megabyte_limit = 1.0
		if filesize > megabyte_limit*1024*1024:
			raise ValidationError("Max file size is %sMB"%str(megabyte_limit))

	title = models.CharField(max_length=500, unique=True)
	image = models.ImageField(upload_to='books/images',validators=[validate_image], blank=True, null=True)
	descriptions = models.TextField(blank=True, null=True)
	author = models.CharField(max_length=125, blank=True)
	slug = models.SlugField(editable=False, allow_unicode=True, unique=True, blank=True)
	iframe = models.TextField(blank=True, null=True)

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
