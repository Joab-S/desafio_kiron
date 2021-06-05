from django.db import models
from django.db.models.deletion import CASCADE
from usuarios.models import User

class Atividade(models.Model):
    titulo = models.CharField(max_length=50, verbose_name= 'Título')
    descricao = models.CharField(max_length=255, verbose_name= 'Descrição')
    criacao = models.DateField(verbose_name= 'Data de criação')

    autor = models.OneToOneField(User, on_delete=CASCADE)

    def __str__(self):
        return ("{}: {} - ({})".format(self.titulo, self.descricao, self.criacao))
        