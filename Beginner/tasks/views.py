from django.shortcuts import render
from django.utils.translation import gettext as _


# Create your views here.
def tasks(request):
	button = '<button class="btn btn-dark" type="button" id="annav" >'+_('hide')+'</button>'
	return render(request, 'tasks/tasks.html',{'hidenav': button})


