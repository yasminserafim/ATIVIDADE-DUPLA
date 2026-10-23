import os
os.system ('cls')

pares = 0
impares = 0
soma = 0

for i in range(5):
    numero = int(input('Digite seu número inteiro: '))

    soma =+ numero

    if numero % 2 == 0:
        pares += 1

    else:
        impares += 1


    print(f'Quantidade de números pares:',{pares})
    print(f'Quantidade de números ímpares:' ,{impares})
    print(f'Soma de todos os números:',{soma})
