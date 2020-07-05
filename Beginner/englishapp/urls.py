from django.urls import path
from .views import EnglishAppView

app_name = 'englishapp'


urlpatterns = [
	path('', EnglishAppView.as_view(), name='english-game'),
]