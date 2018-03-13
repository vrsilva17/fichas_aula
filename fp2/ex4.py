x = int(input('Introduza o coordenado x: '))
y = int(input('Introduza o coordenado y: '))

if x == 0 and y == 0 :
    print('O ponto encontra-se na origem')

elif x > 0 and y > 0 :
    print('O ponto encontra-se no 1ª quadrante')

elif x < 0 and y > 0 :
    print('O ponto encontra-se no 2ª quadrante')

elif x > 0 and y < 0 :
    print('O ponto encontra-se no 3ª quadrante')

elif x < 0 and y < 0 :
    print('O ponto encontra-se no 4ª quadrante')

elif x == 0 :
    print('O ponto encontra-se no eixo dos x')

elif y == 0 :
    print('O ponto encontra-se no eixo dos y')


