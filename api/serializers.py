from . import models
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'date_joined', 'last_login', 'id')


class LabelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Labels
        fields = '__all__'


class CardsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Cards
        fields = '__all__'

# list all the lists but include all the cards on the list


class ListsSerializer(serializers.ModelSerializer):
    cards = CardsSerializer(many=True, read_only=True)

    class Meta:
        model = models.Lists
        fields = '__all__'

# list all the lists (used by BoardsSerializer)


class BoardDetailsSerializer(serializers.ModelSerializer):
    lists = ListsSerializer(many=True, read_only=True)

    class Meta:
        model = models.Boards
        fields = ('id', 'title', 'created', 'last_updated',
                  'archived', 'owner', 'lists')


class BoardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Boards
        fields = '__all__'
