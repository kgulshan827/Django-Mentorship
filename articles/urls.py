from django.urls import path
from . import views

urlpatterns = [
    path('', views.articleList, name="list"),
    path('create', views.create, name="create"),
]