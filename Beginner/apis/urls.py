from django.urls import path
from .views import PersionInfoApiView

app_name = 'apis'

urlpatterns = [
	path('v1/persioninfo/', PersionInfoApiView.as_view(),name='api-test'),
]