from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),  # http://127.0.0.1:8000 - доменное имя
    path('cats/<int:cat_id>/', views.categories),  # http://127.0.0.1:8000/cat/ - url-адрес
    path('cats/<slug:cat_slug>/', views.categories_by_slug),

]
