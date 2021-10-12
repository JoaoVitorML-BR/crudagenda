# Meu primeiro CRUD 

  - Nesse meu primeiro CRUD, foi feito uma agenda parecida com a do celular com opções de adicionar contato,deletar, mover para lista (familia, amigos, trabalho).
  - Esse projeto fiz seguindo o professor Otavio miranda, onde venho aprendendo Python, Django, Banco de dados e Deploy de aplicações por exemplo.
  
## Iniciar

 * para iniciar esse projeto você precisara ter o django instalado na sua maquina. pip install django (talvez seja necessario fazer alguma configuração a mais, caso seja, você ira seguindo os passo a passo que o python for te pedindo)
 
 # Iniciar Servidor
 
  * Para iniciar o servidor você ira digitar: python manage.py runserver (click no Ip/link destacado)
  * abriu o servidor, agora você poderá acessar as áreas de Login, Cadastro, Criar novo contato/ Dashboard.
 
## Criando usuário (comum)

  * acesse o ip do servidor + /accounts/register para registrar um novo usuário. (ficara algo parecido com isso: http://127.0.0.1:8000/accounts/register/)
  * para criar um novo contato, você precisará ter criado esse usuário e estar logado no mesmo, por tanto, após ter feito o registro, logue com o mesmo.
  
## Criando contato
  
  * Após ter criado o usuário e logado, você poderá entrar na Dashboard e criar quantos contatos desejar, bastando acessar: http://127.0.0.1:8000/accounts/dashboard/
  
## SuperUsuário / ADMIN

  * para criar o super usuário ou administrador do site, você deverá rodar o seguinte comando no terminal: python manage.py createsurperuser (e colocar, nome, email e senha)
  * acesse: http://127.0.0.1:8000/admin/ e faça o login, desta forma você terá controle total dos usuários comum, superuser e contatos.
