from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import fields

class User(AbstractUser):
    ####nome = models.CharField(max_length=50)
    #email = models.EmailField()
    ####senha = models.CharField(max_length=50)
    
    #fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        pass

    def __str__(self):
        return self.username