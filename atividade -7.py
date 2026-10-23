import os
os.system( 'cls')

notas = []

for i in range(3):
    nota = float(input(f' Digite a {i+1}° nota: '))

    while nota < 0 or nota > 10:
        print(' Nota inválida! Digite uma nota entre 1 a 10')
        nota = float(input(f'Digite a {i+1}° nota:'))

        notas.append(notas)

media = sum(notas) / 3

print(f'\nmédia: {media:}')

if media >= 7:
    print("APROVADO!")
elif media >= 5:
    print("RECUPERAÇÃO.")
else:
    print("REPROVADO!")
