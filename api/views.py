from rest_framework import views, generics
from rest_framework.response import Response
from rest_framework.views import status
from . import models
from . import serializers

# Create your views here.
# make sure the API is running


class HelloWorld(views.APIView):
    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK,
                        data={'message': 'Hello World'})

# ListCreateAPIView: GET, POST
# RetrieveUpdateDestroyAPIView: GET, PUT, PATCH, DELETE

# Need to be able to list all the boards and create a board


class ListBoards(generics.ListCreateAPIView):
    queryset = models.Boards.objects.all()
    serializer_class = serializers.BoardsSerializer

# Need to be able to list all the lists and create a list


class ListLists(generics.ListCreateAPIView):
    queryset = models.Lists.objects.all()
    serializer_class = serializers.ListsSerializer

# Need to be able to list all the cards and create a card


class ListCards(generics.ListCreateAPIView):
    queryset = models.Cards.objects.all()
    serializer_class = serializers.CardsSerializer

# Need to be able to list all the cards and create a card


class ListLabels(generics.ListCreateAPIView):
    queryset = models.Labels.objects.all()
    serializer_class = serializers.LabelsSerializer

# must be able to perform all actions on a board


class BoardsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Boards.objects.all().prefetch_related()
    serializer_class = serializers.BoardsSerializer

# must be able to perform all actions on a list


class ListsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Lists.objects.all().prefetch_related()
    serializer_class = serializers.ListsSerializer

# must be able to perform all actions on a card


class CardDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Cards.objects.all().prefetch_related()
    serializer_class = serializers.CardsSerializer

# must be able to perform all actions on a card


class LabelDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Labels.objects.all().prefetch_related()
    serializer_class = serializers.LabelsSerializer
