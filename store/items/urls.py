from django.conf.urls import url, include
from django.contrib import admin
from .views import *

app_name = 'item'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)$', ItemDetailView.as_view()),
    url(r'^', ItemCreateAndListView.as_view()),
]