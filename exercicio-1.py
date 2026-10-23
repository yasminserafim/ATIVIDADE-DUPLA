import os
os.system("cls")


numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
operador = str(input("Digite o operador desejado: "))

match operador:
    case "+":
        resultado = numero + segundo_numero
    case "-":
        resultado = numero - segundo_numero
    case "*":
        resultado = numero * segundo_numero
    case "/":
        if numero == 0:
            print("Inválido")
        elif segundo_numero == 0:
            print("Inválido")
        else:
            resultado = numero / segundo_numero
    case _:
        print("Inválido")

print(" = EXIBINDO RESULTADOS = ")
print("Primeiro Número: ", numero)
print("Segundo Número: ", segundo_numero)
print("Operador escolhido: ", operador)
print("Resultado: ", resultado)




