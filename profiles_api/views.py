from rest_framework.utils import serializer_helpers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions, mixins

from profiles_api import serializers

from .models import UserProfile

class HelloApiView(APIView):
    """ API View de prueba"""
    serializer_class= serializers.HelloSerializer

    def get(self, request, format= None):
        """retornar lista de caracteristicas del API View"""

        an_apiview=[
            'Usamos metodos http como funciones (get, post, put, delete)',
            'Similar a vista tradicional del django',
            'da mayor control sobre la logica de la aplicaicon',
            'esta mapeado manualmente a los URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """crea un mensaje con nuestro nombre"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response ({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )


class CreateUserView(
    mixins.CreateModelMixin
    ,viewsets.GenericViewSet):
    
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = serializers.CreateUserSerializer

    def create(self, request, *args, **kwargs):
        """
        Creates a user.
        ---
        example:
            {}
        TODO: Add docstrings for swagger
        """

        serializer = serializers.CreateUserSerializer(data=request.data, context={
            'request': request,
        })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

create_user = CreateUserView.as_view({
    'post': 'create'
})