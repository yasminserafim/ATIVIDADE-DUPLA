import os
os.system('cls')

total = 0
continuar = 's'

while continuar == 's':
    print('\n=== CARDÁPIO ===')
    print('1- LOMBO - R$ 21,00')
    print('2- GALINHA ASSADA - R$ 20,00')
    print('3- LASANHA - R$ 25,00')
    print('4- PORCO - R$ 19,00')
    print('5- BIFE - 20,00')

    codigo = int(input('Escolha o código do prato: '))

    if codigo == 1:
        total += 21
    elif codigo == 2:
        toltal += 20
    elif codigo == 3:
        total += 25
    elif codigo == 4:
        total += 19
    elif codigo == 5:
        total += 20

    else:
        print('Código inválido')

        if codigo >= 1 and codigo <= 5:
            print('Total parcial: R$' ,total)

        continuar = input('Deseja escolher outro prato? (s/n):').lower()

        print('Valor total a pagar: R$', total)