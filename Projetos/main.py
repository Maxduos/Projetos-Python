# import json

def tela_cadastro():

    continuar = True
    cadastrado = False

    while continuar:

        print('Bem vindo ao sistemas de Cadastro de Usuarios!')
        print('Por favor, preencha os campos abaixo para realizar seu cadastro!')
        print('------------------------------------------------------------')
        print('1 - Cadastro')
        print('2 - Login')
        print('3 - Sair')

        opçao =  input('Escolha uma opção: ')

        if opçao == '1':
            nome, login_cadastro, senha_cadastro = cadastro_usuario()
            cadastrado = True
        elif opçao == '2':
             if cadastrado:
                login_usuario(nome, login_cadastro, senha_cadastro)
             else: 
                print('Voce precisa efetuar o cadastro!') 
        elif opçao == '3':
            continuar = False
            print('Saindo do sistema...')
        
def cadastro_usuario():# vai criar uma função para cadastrar o usuario

    print('Bem vindo ao sistema de cadastro de usuarios!')
    nome = str(input('Digite seu nome de Usuario:'))
    login_cadastro =  str(input('Digite seu email para cadastro:'))
    senha_cadastro =  input('Digite a senha para cadastro:')
    senha_confirm = input('Digite novamente sua senha:')

    while senha_cadastro != senha_confirm: # vai criar um loop para verificar se a senha digitada é igual a senha confirmada
        print('As senhas digitadas não são iguais! Por favor, digite novamente a senha de confirmação!')
        senha_confirm = input('confirme sua senha novamente:')
        print('Cadastro realizado com sucesso!')

    return nome, login_cadastro, senha_cadastro  # vai retornar os valores digitados para a função principal que é a tela_cadastro()


def login_usuario(nome, login_cadastro, senha_cadastro): # vai criar uma função para realizar o login do usuario
     email_login = input('Digite seu email para login:')
     senha_login = input('Digite sua senha para login:')
     if email_login == login_cadastro and senha_login == senha_cadastro:
         print('Login realizado com sucesso! Bem vindo {}!'.format(nome))


tela_cadastro()
# dados = {
#       'nome de usuario': nome,
#       'email': login,
#       'senha': senha

# }

# with open('login.json', 'w') as arquivo:
#     json.dump(dados, arquivo, indent=4)