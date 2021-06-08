from django.db import models
from django.db.models.deletion import PROTECT
from usuarios.models import User
from uuid import uuid4

class Atividade(models.Model):
    titulo = models.CharField(max_length=50, verbose_name= 'Título')
    descricao = models.CharField(max_length=255, verbose_name= 'Descrição')
    criacao = models.DateField(verbose_name= 'Data de criação')

    autor = models.ForeignKey(User, on_delete=PROTECT)

    def __str__(self):
        return ("{}: {} - ({})".format(self.titulo, self.descricao, self.criacao))
        