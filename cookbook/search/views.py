from django.template.response import TemplateResponse
from wagtail.contrib.search_promotions.models import Query
from recipes.models import RecipePage


def search(request):
    search_query = request.GET.get('search', None)

    if search_query:
        search_results = RecipePage.objects.live().order_by(
            'title').search(search_query, order_by_relevance=False)
        print(search_results)
        query = Query.get(search_query)
        query.add_hit()
    else:
        search_results = RecipePage.objects.none()

    return TemplateResponse(request, 'search/search.html', {
        'search_query': search_query,
        'search_results': search_results,
    })
