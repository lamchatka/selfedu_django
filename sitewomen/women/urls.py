from django.urls import path, include
from women import views

urlpatterns = [
    path('', views.index),  # http://127.0.0.1:8000 - доменное имя
    path('cats/', views.categories),  # http://127.0.0.1:8000/cat/ - url-адрес
]
