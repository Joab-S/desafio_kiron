from rest_framework import status
from .models import Atividade
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .api.serializers import AtividadeSerializer, CreateAtividadeSerializer
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes ([IsAuthenticated])
def atividades_list_all(request):
    if request.method == 'GET':
        atividadesAll = Atividade.objects.all().order_by('criacao')
        atividades = atividadesAll.filter(autor=request.user.id)
        
        atividades_serializer = AtividadeSerializer(atividades, many=True)
        return JsonResponse(atividades_serializer.data, safe=False)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes ([IsAdminUser])
def atividades_user_name(request): # Buscar todas as atividades por nome de usuario: ADMIN 
    if request.method == 'GET':        
        atividades = Atividade.objects.all().order_by('criacao')
        
        autor = request.query_params.get('autor', None)
        if autor is not None:
            atividades = atividades.filter(titulo__icontains=autor)

        atividades_serializer = AtividadeSerializer(atividades, many=True)
        return JsonResponse(atividades_serializer.data, safe=False)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes ([IsAuthenticated])
def atividades_create(request): # Criar atividade (Necessário um usuario logado)
    if request.method == 'POST':
        atividade_data = JSONParser().parse(request)

        print(atividade_data)
        atividade_data["autor"] = request.user.id
        print(atividade_data)

        atividade_serializer = CreateAtividadeSerializer(data=atividade_data)

        if atividade_serializer.is_valid():
            atividade_serializer.save()
            return JsonResponse(atividade_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(atividade_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
@api_view(['DELETE']) # DELETA TODOS AS ATIVIDADES DE TODOS OS USUARIOS: ADMIN
@authentication_classes([TokenAuthentication])
@permission_classes ([IsAdminUser])
def atividade_delete_all(request):
    if request.method == 'DELETE':
        count = Atividade.objects.all().delete()
        return JsonResponse({'message': '{} Atividades foram deletadas com sucesso.'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
'''

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes ([IsAuthenticated])
def atividade_get_details(request, pk):
    try:
        atividade = Atividade.objects.get(pk=pk)
    except Atividade.DoesNotExist:
        return JsonResponse({'message': 'A atividade não existe.'}, status=status.status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        atividade_serializer = AtividadeSerializer(atividade)
        return JsonResponse(atividade_serializer.data)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes ([IsAuthenticated])
def atividade_put_details(request, pk):
    try:
        atividade = Atividade.objects.get(pk=pk)
    except Atividade.DoesNotExist:
        return JsonResponse({'message': 'A atividade não existe.'}, status=status.status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        atividade_data = JSONParser().parse(request)
        atividade_serializer = AtividadeSerializer(atividade, data=atividade_data)
        
        if atividade_serializer.is_valid():
            atividade_serializer.save()
            return JsonResponse(atividade_serializer.data)
        return JsonResponse(atividade_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes ([IsAuthenticated])
def atividade_delete_details(request, pk):
    try:
        atividade = Atividade.objects.get(pk=pk)
    except Atividade.DoesNotExist:
        return JsonResponse({'message': 'A atividade não existe.'}, status=status.status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        atividade.delete()
        return JsonResponse({'message': 'A atividade foi excluída com sucesso.'}, status=status.HTTP_204_NO_CONTENT)
