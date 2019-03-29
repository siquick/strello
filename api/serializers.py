from . import models
from rest_framework import serializers

class CardsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Cards
        fields = '__all__'

# list all the lists but include all the cards on the 
class ListsSerializer(serializers.ModelSerializer):
    cards = CardsSerializer(many=True,read_only=True)

    class Meta:
        model = models.Lists
        fields = '__all__'

# list all the lists (used by BoardsSerializer)
class ListListsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Lists
        fields = '__all__'

class BoardsSerializer(serializers.ModelSerializer):
    lists = ListListsSerializer(many=True,read_only=True)
    
    class Meta:
        model = models.Boards
        fields = ('pk','title','last_updated','owner','created','lists')



