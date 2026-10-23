import os
os.system("cls")


print(" = BEM-VINDO A FINANCEIRA CONFIA = ")
emprestimo_pedido = float(input("Digite o valor do emprestimo solicitado: "))
renda = float(input("Digite sua renda mensal: "))
prestacoes_pedido = int(input("Digite o número de prestações solicitada: "))


print(" = RESULTADOS = ")
if emprestimo_pedido <= 10 * renda and prestacoes_pedido <= renda * 0.3:
    prestacao = renda * 0.3
    resultado = "Solicitação aceita."
    print(resultado)
    print("Valor da prestação: ", prestacao)
else:
    resultado = "Solicitação negada."
    print(resultado)