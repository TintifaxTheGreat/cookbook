from django.http import HttpResponseRedirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse

from .forms import PortionsForm
from .models import RecipePage, RecipeIndexPage


def change_portions(request):
    if request.method == 'POST':
        form = PortionsForm(request.POST, default_portions='')

        if form.is_valid():
            form.process(request)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    form = PortionsForm()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def recipe_index_paginated(request):
    page = request.GET.get('page')
    next_page = int(page) + 1
    children_sorted = RecipePage.objects.child_of(RecipeIndexPage.objects.first()).live().order_by('title')

    tag = request.GET.get('tag')
    if tag:
        children_sorted = children_sorted.filter(tags__name=tag)

    if page:
        paginator = Paginator(children_sorted, 10)
        try:
            children_sorted = paginator.page(page)
        except PageNotAnInteger:
            children_sorted = paginator.page(1)
        except EmptyPage:
            # children_sorted = paginator.page(paginator.num_pages)
            children_sorted = None
            next_page = None

    return TemplateResponse(request, 'recipes/recipe_index_paginated.html', {
        'children_sorted': children_sorted,
        'page_next': next_page,
        'tag_name': tag,
    })

