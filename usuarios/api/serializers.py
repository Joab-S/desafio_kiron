from usuarios.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from cadastros.models import Atividade

#from django.contrib.auth import get_user_model
#User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    #atividade = serializers.PrimaryKeyRelatedField(many=True, queryset=Atividade.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email']#, 'password']#, 'atividade']

class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class LoginUserSerializer(serializers.Serializer):
    email = serializers.CharField(max_length = 100, required=True)
    password = serializers.CharField(required=True, write_only=True)

class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
        model  = User
        fields = ['id', 'username', 'email', 'auth_token']
        read_only_fields = ['username', 'email']

    def get_auth_token(self, obj):
        token = Token.objects.create(user=obj)
        return (token.key)

class EmptySerializer(serializers.Serializer):
    pass