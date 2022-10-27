from django.template.response import TemplateResponse
from recipes.models import RecipePage
from wagtail.search.models import Query


def search(request):
    search_query = request.GET.get('search', None)

    if search_query:
        search_results = RecipePage.objects.live().search(search_query)
        print(search_results)
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = RecipePage.objects.none()

    return TemplateResponse(request, 'search/search.html', {
        'search_query': search_query,
        'search_results': search_results,
    })
