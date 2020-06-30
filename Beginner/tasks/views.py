from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _


# Create your views here.
def tasks(request):
	button = '<a class="nav-item nav-link btn btn-dark" id="annav" >'+_('hide')+'</a>'
	return render(request, 'tasks/tasks.html',{'hidenav': button})



