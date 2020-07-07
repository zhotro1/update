from django.urls import path
from .views import EnglishAppView, IndexView

app_name = 'englishapp'


urlpatterns = [
	path('', IndexView.as_view(), name='english-home'),
	path('game/', EnglishAppView.as_view(), name='english-game'),
]