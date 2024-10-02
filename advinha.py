from random import randint

N = 0
player1 = 0
player2 = 0

while N < 5:
    numeroescolhido1 = randint(1, 10)
    numeroescolhido2 = randint(1, 10)

    print(f'O numero escolhido pelo player 1 foi: {numeroescolhido1}')
    print(f'O numero escolhido pelo player 2 foi: {numeroescolhido2}')

    if numeroescolhido1 == numeroescolhido2:
        print('Empate')
    elif numeroescolhido1 > numeroescolhido2:
        print('Ponto para o player 1')
        player1 += 1
    elif numeroescolhido1 < numeroescolhido2:
        print('Ponto para o player 2')
        player2 += 1

    print(f'Os pontos do player 1: {player1}')
    print(f"Os pontos do player 2: {player2}\n")
    N += 1

print('P O N TU A Ç Ã O   F I N A L ')
print(f'Os pontos do player 1: {player1}')
print(f"Os pontos do player 2: {player2}")
