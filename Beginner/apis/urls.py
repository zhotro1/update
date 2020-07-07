from django.urls import path
from .views import PersionInfoApiView
from .views import EnglishAppApiView
from .views import EnglishGameScoreApiView

app_name = 'apis'

urlpatterns = [
	path('v1/persioninfo/', PersionInfoApiView.as_view(),name='api-test'),
	path('v1/englishapp/', EnglishAppApiView.as_view(),name='englishapp-api'),
	path('v1/englishscore/', EnglishGameScoreApiView.as_view(),name='englishscore-api'),
]