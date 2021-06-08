from cadastros.models import Atividade
from rest_framework import serializers

class AtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = '__all__' #['ID', 'titulo', 'descricao', 'criacao', 'autor']

class CreateAtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = ['id', 'titulo', 'descricao', 'criacao', 'autor']

