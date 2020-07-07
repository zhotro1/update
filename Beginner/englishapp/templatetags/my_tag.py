from django import template
register = template.Library()

@register.filter
def index(listitem, value):
	i = 1
	for item in listitem:
		if item == value:
			return i
		i += 1
	return ''