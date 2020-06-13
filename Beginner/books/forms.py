from django import forms
from . import models


class BookForm(forms.ModelForm):
    class Meta:
        fields = ("title", "image", "descriptions")
        model = models.Book