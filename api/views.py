from django.shortcuts import render
from rest_framework import views, viewsets, generics
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework import viewsets, permissions
from . import models
from . import serializers

# Create your views here.
# make sure the API is running
class HelloWorld(views.APIView):
    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK,
                            data={'message': 'Hello World'})


class ListBoards(viewsets.ModelViewSet):
    queryset = models.Boards.objects.all()
    serializer_class = serializers.BoardsSerializer

class ListLists(viewsets.ModelViewSet):
    queryset = models.Lists.objects.all()
    serializer_class = serializers.ListsSerializer

class ListCards(viewsets.ModelViewSet):
    queryset = models.Cards.objects.all()
    serializer_class = serializers.CardsSerializer

class BoardsDetail(generics.RetrieveAPIView):
    queryset = models.Boards.objects.all().prefetch_related()
    serializer_class = serializers.BoardsSerializer

class ListsDetails(generics.RetrieveAPIView):
    queryset = models.Lists.objects.all().prefetch_related()
    serializer_class = serializers.ListsSerializer
