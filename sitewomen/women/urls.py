from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),  # http://127.0.0.1:8000 - доменное имя
    path('cats/<int:cat_id>/', views.categories, name='cat_by_id'),  # http://127.0.0.1:8000/cat/ - url-адрес
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cat_by_slug'),
    path('archive/<year4:year>/', views.archive, name='archive')

]
