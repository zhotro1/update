from django.contrib import admin
from .models import EnglishAppModel

# Register your models here.
class EnglishAdmin(admin.ModelAdmin):
	list_display = ('card_name', 'card_pic', 'card_voice')
	list_filter = ('card_name',)
	search_fields = ('card_name',)

admin.site.register(EnglishAppModel, EnglishAdmin)
