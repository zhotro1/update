from django.urls import path
from .views import PersionInfoApiView
from .views import EnglishAppApiView

app_name = 'apis'

urlpatterns = [
	path('v1/persioninfo/', PersionInfoApiView.as_view(),name='api-test'),
	path('v1/englishapp/', EnglishAppApiView.as_view(),name='englishapp-api'),
]