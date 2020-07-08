from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import EnglishAppModel, EnglishGameScoreModel
import json, random, datetime
from rest_framework.authtoken.models import Token


# Create your views here.
def get_to_day_min():
	return datetime.datetime.combine(datetime.date.today(), datetime.time.min).timestamp()


class IndexView(ListView):
	template_name = 'englishapp/index.html'
	context_object_name = 'top10'
	model = EnglishGameScoreModel

	def get_queryset(self):
		queryset = EnglishGameScoreModel.objects.filter(time_update_score__gte=get_to_day_min()).order_by("score").reverse()[:10]
		return queryset


class EnglishAppView(TemplateView):
	template_name = 'englishapp/game.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		if self.request.user.is_authenticated:
			context['token'] = Token.objects.get(user=self.request.user)
		return context
