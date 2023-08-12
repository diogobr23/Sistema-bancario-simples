# Sistema Bancário 2

# Criar duas novas funções:
## cadastrar usuário (cliente)
####
## cadastrar conta corrente (vincular com o cliente)
####

# Criar funções para as operações existentes: 
## sacar
#### - (keyword only)
#### - Argumentos: (saldo, valor, extrato, limite, numero_saques, limite_saques)
#### - Retorno: saldo e extrato
## depositar
#### - (positioinal only)
#### - Argumentos: (saldo, valor, extrato)
#### - Retorno: saldo e extrato
## extrato
#### - (position only e keyword only)
#### - Argumentos posicionais: (saldo e argumentos nomeados: extrato).
#### - Retorno: saldo e extrato


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Nova conta
[n] Novo cliente
[q] Sair

=> """

# definição das funções sacar, depositar e extrato
def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if valor < 0:
        print('\nA operação falhou! Informe um valor positivo.\n')
    if valor > limite:
        print(f'\nA operação falhou! Informe um valor menor que o limite de R$ {limite:.2f}.\n')
    if numero_saques > LIMITE_SAQUES:
        print(f'\nA operação falhou! O limite de {LIMITE_SAQUES} saques foi atingido.\n')
    if valor < saldo:
        print (f'\nA operação falhou! Saldo insuficiente (R$ {saldo:.2f})\n')
    else:
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f'\nSaque efetuado no valor de R$ {valor:.2f}\n')
    return saldo, extrato

def depositar(saldo, valor, extrato, \):
    if valor < 0:
        print ('\nA operação falhou! Informe um valor positivo.\n')
    else:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"\nVocê depositou R$ {valor:.2f}\n")
    
    return saldo, extrato

def extrato(saldo, extrato):
    print("\nEXTRATO:\n")
        print("Nenhuma movimentação foi efetuada." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}\n")
    return saldo, extrato


#####
# ###
# ###
# ###


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\nVocê depositou R$ {valor:.2f}\n")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f'\nSaque efetuado no valor de R$ {valor:.2f}\n')

        else:
            print("\nO valor informado é inválido.\n")

    elif opcao == "e":
        print("\nEXTRATO:\n")
        print("Nenhuma movimentação foi efetuada." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n")
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")