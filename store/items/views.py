from django.shortcuts import render
from rest_framework import generics
from .serializers import ItemDetailSerializer, ItemDetailEditSerializer
from .models import Item
# Create your views here.

class ItemCreateView(generics.CreateAPIView):
    serializer_class = ItemDetailSerializer

class ItemsListView(generics.ListAPIView):
    serializer_class = ItemDetailSerializer
    queryset = Item.objects.all()

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemDetailEditSerializer
    queryset = Item.objects.all()