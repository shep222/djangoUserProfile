from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HHTP methods as functions (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Give you the most control over your logic',
            'Is mappaed manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """create a hello messge with our name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """put requst"""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provied in the request"""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """delete on object"""

        return Response({'method': 'delete'})
