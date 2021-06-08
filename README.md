
<h3> Desafio Kiron </h3>

<h2> Rotas </h2>


-api/get/usuario: Exibe todos os usuários

-api/name/usuario: Permite pesquisar por um usuário pelo nome

-api/post/usuario$: Permite criar novos usuários

-api/put/usuario/(?P<pk>[0-9]+): Possibilita atualizar um usuário pelo id
  
-api/delete/usuario/(?P<pk>[0-9]+): Possibilita deletar um usuário pelo id
  
-api/get/atividade: Lista de todas as atividades de um usuário por data de criação
  
-api/autor/atividade: Pesquisa as atividades de um usuario pelo seu nome
  
-api/post/atividade: Permite registrar novas atividades 
  
-api/get/atividade-id/(?P<pk>[0-9]+): Busca atividades por ID 
  
-api/put/atividade-id/(?P<pk>[0-9]+): Atualiza atividades por ID
  
-api/delete/atividade-id/(?P<pk>[0-9]+): Deleta atividades por ID
  
-api/auth/login: Permite ao usuário fazer login no sistema (recebe um token como reposta)
  
  
NOTA: Todas as entradas (exceto cadastro e login) pedem algum tipo de autenticação, sendo que para os endpois de usuários, grande parte é necessaria permissão de administrador, mas para atividades um login de usários é suficiente.
