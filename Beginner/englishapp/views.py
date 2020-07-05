from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import EnglishAppModel
import json, random

# Create your views here.
class EnglishAppView(LoginRequiredMixin, ListView):
	model = EnglishAppModel
	context_object_name = 'cards'
	template_name = 'englishapp/game.html'

	def get_queryset(self):
		queryset = EnglishAppModel.objects.all().order_by("?")[:6]
		return queryset

	def get_context_data(self, **kwargs):
		objects = EnglishAppModel.objects.all()
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['nana'] = random.choice(context['cards'])
		return context
