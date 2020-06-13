from django.shortcuts import render
from django.views import generic
from .models import Book

# Create your views here.
class BookIndex(generic.ListView):
	model = Book
	context_object_name = 'books'
	template_name = 'books/book_list.html'
	paginate_by = 10
	ordering = ['title']
	def get_queryset(self):
		name = self.request.GET.get('q')
		if name:
			object_list = self.model.objects.filter(title__icontains = name)
		else:
			object_list = self.model.objects.all()
		return object_list


class BookDetail(generic.DetailView):
	model = Book
	context_object_name = 'book'
	template_name = 'books/book_detail.html'