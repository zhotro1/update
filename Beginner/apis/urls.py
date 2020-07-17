from django.urls import path
from .views import PersionInfoApiView
from .views import EnglishGameApiView
from .views import EnglishGameScoreApiView
from .views import EnglishGameManagerApiView

app_name = 'apis'

urlpatterns = [
	path('v1/persioninfo/', PersionInfoApiView.as_view(),name='api-test'),
	path('v1/englishgame/', EnglishGameApiView.as_view(),name='englishgame-api'),
	path('v1/englishscore/', EnglishGameScoreApiView.as_view(),name='englishscore-api'),
	path('v1/englishmanager/', EnglishGameManagerApiView.as_view(),name='englishmanager-api'),
]