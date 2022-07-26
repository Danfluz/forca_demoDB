from random import randint

animais = ['gato', 'cavalo', 'cabra', 'cachorro', 'porco', 'pato', 'vaca', 'boi', 'bode', 'ovelha', 'cobra', 'ganso']


def aleatorio(lista):
    aleatorio = lista[randint(0, len(lista) - 1)]

    return aleatorio


animal = aleatorio(animais)

print('\t== Jogo da Forca ==')
print('')
print('Bem vindo ao jogo da forca!\nEm um teste para o Start DB, vamos tentar descobrir qual a palavra secreta.'
      '\n(Você terá 4 chances)\n\n\n')

digitados = []
chance = 4
secreto_temporario = ''

while True:
    if secreto_temporario == '':
        secreto_temporario = " ".join(("_" * len(animal)))
    print(f'Palavra: {secreto_temporario}')
    secreto_temporario = ''
    print(f'\nDica: Animal doméstico com {len(animal)} letras.\n')
    print('\t\tLetras utilizadas: ', *digitados)
    print('')
    letra = input('Digite uma letra: ')
    print('')

    if len(letra) > 1:
        print('Assim não vale. Só pode digitar 1 letra por vez.')
        print('')
        continue

    elif len(letra) < 1:
        print('ERRO: Você não digitou nada.')
        print('')
        continue

    elif letra.isdigit():
        print('ERRO: Apenas letras são permitidas.')
        print('')
        continue

    else:
        digitados.append(letra.upper())

    for letra_secreta in animal:

        if letra_secreta.upper() in digitados:
            secreto_temporario += letra_secreta

        else:
            secreto_temporario += ' _ '

    if letra in animal:
        print(f'\nSim, a palavra contém a letra {letra}\n')

    else:
        print(f'Que pena, a palavra não contém a letra {letra}!')
        chance = chance - 1
        print(f'Chances restantes: {chance}\n')

    if chance == 3:
        print('')
        print('• • • • ,---------,')
        print('• • • • O • • • • |')
        print('• • • • | • • • • |')
        print('• • • • • • • • • |')
        print('• • • • • • • • • |')
        print('• • • • • • • • •==')
        print('')

    if chance == 2:
        print('')
        print('• • • • ,---------,')
        print('• • • • O • • • • |')
        print('• • • •/|\• • • • |')
        print('• • • • • • • • • |')
        print('• • • • • • • • • |')
        print('• • • • • • • • •==')

    if chance == 1:
        print('')
        print('• • • • ,---------,')
        print('• • • • O • • • • |')
        print('• • • •/|\• • • • |')
        print('• • • •/  • • • • |')
        print('• • • • • • • • • |')
        print('• • • • • • • • •==')

    if chance == 0:
        print('')
        print('• • • • ,---------,')
        print('• • • • O • • • • |')
        print('• • • •/|\ • • • •|')
        print('• • • •/ \ • • • •|')
        print('• • • • • • • • • |')
        print('• • • • • • • • •==')
        print("Aaaahh.....")
        print(f'Você perdeu. A palavra secreta era: {animal}')
        print('FIM DE JOGO')
        break

    if secreto_temporario == animal:
        print('')
        print(f'Parabéns, você ganhou! A palavra era: {animal}.')
        break

print('\nSe gostou, não se esqueça de me selecionar: Danilo Feliciano Luz')
print('Pressione enter para encerrar.')
input()
