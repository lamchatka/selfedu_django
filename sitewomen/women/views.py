from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse


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


def archive(request, year):
    if year > 2025:
        uri = reverse('cat_by_slug', args=('music',))
        return redirect(uri)

    return HttpResponse(f"<h1>Архив по годам</h1><p>year: {year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
