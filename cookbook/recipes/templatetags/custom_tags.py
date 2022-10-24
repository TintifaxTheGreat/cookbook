from django import template

register = template.Library()


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

    if k==0:
        return None

    return value / k
