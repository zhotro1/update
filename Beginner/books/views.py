from django.shortcuts import render
from django.views import generic
from .models import Book
from django.utils.translation import gettext as _

# Create your views here.
class BookIndex(generic.ListView):
	model = Book
	context_object_name = 'books'
	template_name = 'books/book_list.html'
	paginate_by = 10
	ordering = ['title']
	def get_context_data(self, **kwargs):
	    context = super(BookIndex, self).get_context_data(**kwargs)
	    context['searchnav'] ='''<form class="form-inline my-2 my-lg-0" action="#" method="GET">
      <input class="form-control mr-sm-2" type="search" placeholder="'''+_("Name of book")+'''" aria-label="Find the book" name='q'>
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">'''+_("Search")+'''</button>
    </form>'''
	    return context

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