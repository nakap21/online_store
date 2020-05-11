from django.conf.urls import url, include
from django.contrib import admin
from .views import *

app_name = 'item'
urlpatterns = [
    url(r'^item/create/', ItemCreateView.as_view()),
    url(r'^all/', ItemsListView.as_view()),
    url(r'^item/detail/(?P<pk>[0-9]+)$', ItemDetailView.as_view()),
]