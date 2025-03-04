from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """
    Возвращает главную страницу
    """
    return HttpResponse("Hello world!")


def categories(request):
    return HttpResponse("<h1>Страница категорий</h1>")
