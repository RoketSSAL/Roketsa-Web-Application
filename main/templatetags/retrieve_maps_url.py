
from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter
@stringfilter
def retrieve_maps_url(query):
    return f'https://www.google.com/maps/search/?api=1&query={query}'
