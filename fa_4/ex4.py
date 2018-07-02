num_alunos = 10
min = 0
max = 20

def lerinteiro(min,max) : 
    num = min - 1
    while num < min or num > max :
        num = int(input('Introduza um numero inteiro: '))
    return num

def lernotas(num) :
    soma = 0
    num = lerinteiro(0,20)
    soma += num
    return soma

def media(soma) :
    soma = lernotas(soma)
    media = soma / 10
    return media

lerinteiro(0,20)

print('A média é: ', media)
