from urllib.parse import quote_plus
from django import template

# This will allowed you to share the link

register = template.Library()


@register.filter
def urlify(value):
	return quote_plus(value)