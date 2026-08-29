import json

nome = str(input('Digite seu nome de Usuario::'))
login =  str(input('Digite seu email para cadastro:'))
senha =  input('Digite a senha para cadastro:')
senha_confirm = input('Digite novamente sua senha:')


if senha == senha_confirm:
        print('Senha confirmada com sucesso!')
else: 
    print('Senha não confere, tente novamente!')

print('Cadastro realizado com sucesso!' ' Olá {}!'.format(nome))

dados = {
      'nome de usuario': nome,
      'email': login,
      'senha': senha

}

with open('login.json', 'w') as arquivo:
    json.dump(dados, arquivo, indent=4)