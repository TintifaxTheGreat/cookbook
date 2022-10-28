import math
from django import template

from recipes.models import RecipePage

register = template.Library()


@register.inclusion_tag('recipes/taglist.html', takes_context=True)
def taglist(context):
    return {
        'tags': RecipePage.get_all_tags(),
        'request': context['request'],
    }


@register.filter(name='calculate_portions')
def calculate_portions(value, request):
    if not value:
        return None

    if 'portions' not in request.session:
        portions = 4
    else:
        portions = request.session['portions']

    return value * portions


@register.filter(name='div')
def divide_by(value, k):
    if not value:
        return None

    if isinstance(value, str):
        value = math.floor(float(value))
    if isinstance(k, str):
        value = math.floor(float(k))

    if k == 0:
        return None

    return value / k
