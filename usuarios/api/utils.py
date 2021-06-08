#from django.contrib.auth import authenticate
from rest_framework import serializers
from usuarios.models import User
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.backends import ModelBackend

from passlib.hash import pbkdf2_sha256

#from django.contrib.auth import get_user_model
#User = get_user_model()

class EmailBackend(ModelBackend):
    def get_and_authenticate_user(email, password):

        try:
            user = User.objects.get(email = email)
            
        except User.DoesNotExist:
            raise serializers.ValidationError("Email incorreto, tente novamente.")

        else:
            # CRIPTOGRAFIA #
            #if pbkdf2_sha256.verify(password, user.password):
            if password == user.password:
                return user
            else:
                raise serializers.ValidationError("Senha incorreta, tente novamente.")