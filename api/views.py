from . import serializers
from rest_framework import views, generics
from rest_framework.response import Response
from rest_framework.views import status
from . import models
from django.contrib.auth import get_user_model
User = get_user_model()


class HelloWorld(views.APIView):
    def get(self, *args, **kwargs):
        return Response(status=status.HTTP_200_OK,
                        data={'message': 'Hello World'})


# ListCreateAPIView: GET, POST
# RetrieveUpdateDestroyAPIView: GET, PUT, PATCH, DELETE


class ListBoards(generics.ListCreateAPIView):
    queryset = models.Boards.objects.all()
    serializer_class = serializers.BoardsSerializer


class ListLists(generics.ListCreateAPIView):
    queryset = models.Lists.objects.all()
    serializer_class = serializers.ListsSerializer


class ListCards(generics.ListCreateAPIView):
    queryset = models.Cards.objects.all()
    serializer_class = serializers.CardsSerializer


class ListLabels(generics.ListCreateAPIView):
    queryset = models.Labels.objects.all()
    serializer_class = serializers.LabelsSerializer


class ListUsers(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UsersSerializer


class BoardsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Boards.objects.all().prefetch_related()
    serializer_class = serializers.BoardDetailsSerializer


class ListsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Lists.objects.prefetch_related()
    serializer_class = serializers.ListsSerializer


class CardDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Cards.objects.all().prefetch_related()
    serializer_class = serializers.CardsSerializer


class LabelDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Labels.objects.all().prefetch_related()
    serializer_class = serializers.LabelsSerializer


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().prefetch_related()
    serializer_class = serializers.UsersSerializer
