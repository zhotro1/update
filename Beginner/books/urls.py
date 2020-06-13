from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('',views.BookIndex.as_view(), name='book-index'),
    path('detail/<slug:slug>/', views.BookDetail.as_view(), name='book-detail'),
]