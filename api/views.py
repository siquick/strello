from django.shortcuts import render
from rest_framework import views, generics
from rest_framework.response import Response
from rest_framework.views import status

# Create your views here.
# make sure the API is running
class HelloWorld(views.APIView):
    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK,
                            data={'success': 'true'})