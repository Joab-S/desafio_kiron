from django.core.exceptions import ImproperlyConfigured
from rest_framework.authentication import TokenAuthentication
from usuarios.api.utils import EmailBackend
from rest_framework import serializers, viewsets, status

#from .models import User
from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework.decorators import api_view, action, authentication_classes, permission_classes
from .api.serializers import AuthUserSerializer, EmptySerializer, LoginUserSerializer, RegisterUserSerializer, UserSerializer
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from django.contrib.auth.hashers import make_password
from passlib.hash import pbkdf2_sha256

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes ([IsAdminUser])
def user_list_all(request):
    if request.method == 'GET':
        usuarios = User.objects.all()
        
        usuarios_serializer = UserSerializer(usuarios, many=True)
        return JsonResponse(usuarios_serializer.data, safe=False)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes ([IsAdminUser])
def user_name(request):
    if request.method == 'GET':
        usuarios = User.objects.all()        
        nome = request.query_params.get('nome', None)
        
        if nome is not None:
            usuario = usuarios.filter(username__icontains=nome)

        usuario_serializer = UserSerializer(usuario,  many=True)
        return JsonResponse(usuario_serializer.data, safe=False)

@api_view(['POST'])
def user_create(request):
    if request.method == 'POST':
        usuario_data = JSONParser().parse(request)

        # CRIPTOGRAFIA #

        #u = str(pbkdf2_sha256.encrypt(usuario_data['password'], rounds = 120000, salt_size=32))
        #usuario_data['password'] = u
        #print(usuario_data['password'])
        
        usuario_serializer = RegisterUserSerializer(data=usuario_data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse(usuario_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
"""
@api_view(['DELETE'])
def user_delete_all(request):
    if request.method == 'DELETE':
        count = User.objects.all().delete()
        return JsonResponse({'message': '{} Usuários foram deletados com sucesso.'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
"""

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes ([IsAdminUser])
def user_get_details(request, pk):
    try:
        usuario = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse({'message': 'O usuario não existe.'}, status=status.status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        usuario_serializer = UserSerializer(usuario)
        return JsonResponse(usuario_serializer.data)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes ([IsAdminUser])
def user_put_details(request, pk):
    try:
        usuario = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse({'message': 'O usuário não existe.'}, status=status.status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        usuario_data = JSONParser().parse(request)
        usuario_serializer = UserSerializer(usuario, data=usuario_data)
        
        if usuario_serializer.is_valid():
            usuario_serializer.set_password('new password')
            usuario_serializer.save()
            return JsonResponse(usuario_serializer.data)
        return JsonResponse(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes ([IsAdminUser])
def user_delete_details(request, pk):
    try:
        usuario = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse({'message': 'O usuário não existe.'}, status=status.status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        usuario.delete()
        return JsonResponse({'message': 'O usuário foi excluído com sucesso.'}, status=status.HTTP_204_NO_CONTENT)


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = EmptySerializer
    serializer_classes = {
        'login': LoginUserSerializer,
    }

    @action(methods=['POST',], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = EmailBackend.get_and_authenticate_user(**serializer.validated_data)
        data = AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_200_OK)
    
    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes deve ser um dicionário.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()