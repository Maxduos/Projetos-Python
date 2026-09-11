# import json

def tela_cadastro():
    print('Bem vindo ao sistemas de Caddastro de Usuarios!')
    print('Por favor, preencha os campos abaixo para realizar seu cadastro!')
    print('------------------------------------------------------------')
    print('1 - Login')
    print('2 - Cadastro')
    print('3 - Sair')

    opçao =  (input('Escolha uma opção: '))

    if opçao == '1':
        print( 'area de login')
    elif opçao == '2':
        print(cadastro_usuario())
    elif opçao == '3':
        print('Saindo do sistema...')

tela_cadastro()

def cadastro_usuario():

    print('Bem vindo ao sistema de cadastro de usuarios!')
    nome = str(input('Digite seu nome de Usuario:'))
    login_cadastro =  str(input('Digite seu email para cadastro:'))
    senha_cadastro =  input('Digite a senha para cadastro:')
    senha_confirm = input('Digite novamente sua senha:')


    if senha_cadastro == senha_confirm:
            print('Senha confirmada com sucesso!')
    else: 
        print('Senha não confere, tente novamente!')

    print('Cadastro realizado com sucesso!' ' Olá {}!'.format(nome))

cadastro_usuario()

def login_usuario():
     print('Seja bem vindo ao sistema de login de usuarios!')
     email = str(input('Digite seu email para login:'))
     senha = input('Digite sua senha para login:')
     if email == login_cadastro and senha == senha_cadastro:
          print('login efetuado com sucesso! Olá {}!'.format(nome))

# dados = {
#       'nome de usuario': nome,
#       'email': login,
#       'senha': senha

# }

# with open('login.json', 'w') as arquivo:
#     json.dump(dados, arquivo, indent=4)