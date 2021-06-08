'''
from django.conf.urls import url
from .views import atividades_details, atividades_list 

urlpatterns = [
    url(r'^api/atividade$', atividades_list, name = 'AtividadeAll'),
    url(r'^api/atividade/(?P<pk>[0-9]+)$', atividades_details, name = 'AtividadeDetails'),
    #path('api/atividade/autor/', atividades_list, name = 'AtividadeCreate'),
]

##  METODO    |       ENDPOINTS         |            FUNÇÕES              ##
##____________|_________________________|_________________________________##
##  POST:     |   api/atividade/        |   Criar nova atividade          ##
##  GET:      |   api/atividade/        |   Listar todas as atividades    ##
##  DELETE:   |   api/atividade/        |   Deletar todas as atividades   ##
##  GET:      |   api/atividade/id/     |   Buscar   atividade  por ID    ##
##  DELETE:   |   api/atividade/id/     |   Deletar atividade  por  ID    ##
##  PUT:      |   api/atividade/id/     |   Atualizar atividade por ID    ##
##  GET:      |   api/atividade/autor/  |   Buscar atividade por autor    ##
##  PUT:      |   api/atividade/autor/  |   Atualizar atividade por autor ##
'''

from django.conf.urls import url
from .views import atividade_get_details, atividade_put_details, atividades_list_all, atividades_create, atividade_delete_details, atividades_user_name

urlpatterns = [
    url(r'^api/get/atividade$', atividades_list_all, name = 'AtividadeGetAll'),
    url(r'^api/autor/atividade$', atividades_user_name, name = 'AtividadeAutor'),
    url(r'^api/post/atividade$', atividades_create, name = 'AtividadeCreate'),
    
    #url(r'^api/atividade$', atividade_delete_all, name = 'AtividadeDeleteAll'),
    
    url(r'^api/get/atividade-id/(?P<pk>[0-9]+)$', atividade_get_details, name = 'AtividadeGetID'),
    url(r'^api/put/atividade-id/(?P<pk>[0-9]+)$', atividade_put_details, name = 'AtividadePutID'),
    url(r'^api/delete/atividade-id/(?P<pk>[0-9]+)$', atividade_delete_details, name = 'AtividadeDeleteID'),
]

##  METODO    |       ENDPOINTS         |            FUNÇÕES              ##
##____________|_________________________|_________________________________##
##  POST:     |   api/atividade/        |   Criar nova atividade          ##
##  GET:      |   api/atividade/        |   Listar todas as atividades    ##
##  DELETE:   |   api/atividade/        |   Deletar todas as atividades   ##
##  GET:      |   api/atividade/id/     |   Buscar   atividade  por ID    ##
##  DELETE:   |   api/atividade/id/     |   Deletar atividade  por  ID    ##
##  PUT:      |   api/atividade/id/     |   Atualizar atividade por ID    ##
##  GET:      |   api/atividade/autor/  |   Buscar atividade por autor    ##
##  PUT:      |   api/atividade/autor/  |   Atualizar atividade por autor ##
