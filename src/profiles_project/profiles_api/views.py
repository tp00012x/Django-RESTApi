from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import HelloSerializer
# Create your views here.


class HelloApiView(APIView):
    '''Test Api view.'''

    serializer_class = HelloSerializer

    def get(self, request, format=None):
        '''Returns a list of APIView features'''

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        '''Create a hello message with out name.'''

        serializer = HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        '''Handles updating an object.'''

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        '''Path request, only updates fields provide in the request.'''

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):

        return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):
    '''Test API View set.'''

    def list(self, request):
        '''Return a hello message'''

        a_viewset = [
            'Uses actions (list, create retrieve, update, partial_update',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code.',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})