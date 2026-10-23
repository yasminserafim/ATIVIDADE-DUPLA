import os
os.system("cls")


print('''
= ATAKAREJO BOM PREÇO = 
ARROZ R$ 3,00
FEIJÃO R$ 3,50
MACARRAO = 4,20
ÁGUA = 2,50
========================
''')


while True:
    pedido = str(input("Digite o seu pedido: "))
    quantidade = int(input("Digite a quantidade: "))
    opcao_outro_pedido = str(input("Deseja fazer mais um pedido? "))
    if opcao_outro_pedido == "sim":
        segundo_pedido = str(input("Digite o seu pedido: "))
        segunda_quantidade = int(input("Digite a quantidade: "))
        opcao_outro_pedido = str(input("Deseja fazer mais um pedido? "))
        if opcao_outro_pedido == "nao":
            break
    else:
        break


match pedido:
    case "arroz":
        preco = 3 * quantidade
    case "feijao":
        preco = 3.50 * quantidade
    case "macarrao":
        preco = 4.20 * quantidade
    case "agua":
        preco = 2.50 * quantidade
    case _:
        print("Inválido")


if quantidade <= 5:
    desconto = "2%"
    total = preco * 0.02
    total_pagar = preco - total
elif quantidade <= 10:
    desconto = "3%"
    total = preco * 0.03
    total_pagar = preco - total
else:
    desconto = "5%"
    total = preco * 0.05
    total_pagar = preco - total

print(" = EXIBINDO RESULTADOS = ")
print("Pedidos: ", pedido)
print("Total: ", preco)
print("Desconto: ", desconto)
print("Total a pagar: ", total_pagar)