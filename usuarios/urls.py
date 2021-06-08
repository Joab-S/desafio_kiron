from django.conf.urls import url
from django.urls import path
from .views import user_create, user_delete_details, user_get_details, user_list_all, user_put_details, user_name

urlpatterns = [
    path('api/get/usuario', user_list_all, name = 'UserGetAll'),
    url(r'^api/name/usuario$', user_name, name = 'UserName'),
    url(r'^api/post/usuario$', user_create, name = 'UserCreate'),
    url(r'^api/put/usuario/(?P<pk>[0-9]+)$', user_put_details, name = 'UserPut'),
    url(r'^api/delete/usuario/(?P<pk>[0-9]+)$', user_delete_details, name = 'UserDelete'),
]
