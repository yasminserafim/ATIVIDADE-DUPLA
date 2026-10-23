import os
os.system("cls")


print('''
=== MUNDO ELETRO ===
> CAIXA:
''')
valor = float(input("Digite o valor do produto: "))
print("OPÇÕES DE PAGAMENTO: 1 PARA Á VISTA, 2 PARA A PRAZO.")
opcao_pagamento = int(input("Digite sua opção de pagamento: "))

match opcao_pagamento:
    case 1:
        desconto = valor * 0.1
        total = valor - desconto
        print("=== EXIBINDO RESULTADOS ===")
        print("Valor do produto: ", valor)
        print("Forma de pagamento: ", opcao_pagamento)
        print("Desconto: ", desconto)
        print("Total: ", total)
    case 2:
        parcelas = int(input("Digite a quantidade de parcelas (max 6): "))
        total = valor / parcelas
        if parcelas >6:
            print("Valor inválido.")
        print("=== EXIBINDO RESULTADOS ===")
        print("Valor do produto: ", valor)
        print("Forma de pagamento: ", opcao_pagamento)
        print("Parcelas: ", parcelas)
        print("Total: ", total)
    case _:
        print("Inválido.")
