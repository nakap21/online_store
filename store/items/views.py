from rest_framework import generics
from .serializers import ItemDetailSerializer, ItemDetailEditSerializer
from .models import Item
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class ItemCreateView(generics.CreateAPIView):
    serializer_class = ItemDetailSerializer

class ItemsListView(generics.ListAPIView):
    serializer_class = ItemDetailSerializer
    queryset = Item.objects.all()

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemDetailEditSerializer
    queryset = Item.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        serial = self.get_serializer(instance)
        self.perform_destroy(instance)
        return Response(data=serial.data, status=status.HTTP_200_OK)
