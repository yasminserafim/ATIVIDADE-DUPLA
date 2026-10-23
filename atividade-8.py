import os
os.system('cls')


# CADASTRO DE BLOQUEIO.

print('=== CADASTRO- CLÍNICA VIDA PLENA === ')
login_cadastrado = input(' Cadastre seu login: ')
senha_cadastrada = input(' Cadastre sua senha: ')

os.system('cls' if os.name == 'nt' else 'clear')

# LOGIN DE TENTATIVAS.

tentativas_restantes = 3
while tentativas_restantes > 0:

    print('=== LOGIN DA CLÍNICA VIDA PLENA ===')
    login_informado = input('login')
    senha_informada = input(' senha')

    if login_informado == login_cadastrado and senha_informada == senha_cadastrada:
        print('/n SEJA BEM VINDO AO PORTAL.')
        break

    else:
        tentativas_restantes  -= 1
        print('/n login ou senha incorretas!')

    if tentativas_restante == 0:
        print('ACESSO BLOQUEADO! NÚMERO MÁXIMO ALCANÇADO.')