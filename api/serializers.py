from . import models
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login')

class LabelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Labels
        fields = '__all__'


class CardsSerializer(serializers.ModelSerializer):
    labels = LabelsSerializer(many=True, read_only=True)

    class Meta:
        model = models.Cards
        fields = (
            'pk',
            'title',
            'last_updated',
            'owner',
            'created',
            'list',
            'assignee',
            'position',
            'labels')

# list all the lists but include all the cards on the


class ListsSerializer(serializers.ModelSerializer):
    cards = CardsSerializer(many=True, read_only=True)

    class Meta:
        model = models.Lists
        fields = '__all__'

# list all the lists (used by BoardsSerializer)


class ListListsSerializer(serializers.ModelSerializer):
    cards = CardsSerializer(many=True, read_only=True)
    class Meta:
        model = models.Lists
        fields = '__all__'


class BoardsSerializer(serializers.ModelSerializer):
    lists = ListListsSerializer(many=True, read_only=True)
    labels = LabelsSerializer(many=True, read_only=True)

    class Meta:
        model = models.Boards
        fields = (
            'pk',
            'title',
            'last_updated',
            'owner',
            'created',
            'lists',
            'labels')
