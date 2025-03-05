from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    """
    Возвращает главную страницу
    """
    return HttpResponse("Hello world!")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Страница категорий</h1><p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)  # <QueryDict: {'name': ['Gagarina'], 'type': ['pop']}>
    return HttpResponse(f"<h1>Страница категорий</h1><p>slug: {cat_slug}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")