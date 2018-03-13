num1 = float(input('Introduza o 1 valor: '))
num2 = float(input('Introduza o 2 valor: '))

opcao = input('Clique no carater da operação que deseja realizar? ')

if opcao == '+' :
    resultado = num1 + num2
if opcao == '-' :
    resultado = num1 - num2
if opcao == '*' :
    resultado = num1 * num2
if opcao == '/' :
    resultado = num1 / num2

print('O resultado é: ', resultado)
