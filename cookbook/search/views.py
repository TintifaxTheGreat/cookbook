from django.http import JsonResponse
from django.template.response import TemplateResponse
from wagtail.contrib.search_promotions.models import Query
from recipes.models import RecipePage


def search(request):
    search_query = request.GET.get("search", None)

    if search_query:
        search_results = (
            RecipePage.objects.live()
            .order_by("title")
            .search(search_query, order_by_relevance=False)
        )
        query = Query.get(search_query)
        query.add_hit()
    else:
        search_results = RecipePage.objects.none()

    return TemplateResponse(
        request,
        "search/search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
        },
    )


def search_autocomplete(request):
    search_query = request.GET.get("query", None)

    if search_query:
        search_results = RecipePage.objects.live().autocomplete(
            search_query, order_by_relevance=True
        )
        results = [
            {"title": search_result.title, "url": search_result.url}
            for search_result in search_results[:5]
        ]
    else:
        results = []

    return JsonResponse({"results": results})
