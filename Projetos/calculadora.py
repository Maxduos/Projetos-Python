print('CALCULADORA')
n1 = float(input('Digite um nuemro:'))
n2 = float(input('Digite outro numero:'))
tipo_sinal = input('Digite qual operação voce deseja realizar (+, *, /, -) ')
resultado = 0
if tipo_sinal == '+':
    resultado = n1 + n2
elif tipo_sinal == '-':
    resultado = n1 - n2
elif tipo_sinal == '/':
    resultado = n1 / n2
elif tipo_sinal == '*':
    resultado = n1 * n2
print('O resultado da operação é: {}'.format(resultado)) 