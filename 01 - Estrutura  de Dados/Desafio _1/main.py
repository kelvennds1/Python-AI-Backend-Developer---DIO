menu = """

[d] = deposito
[s] = sacar
[e] = extrato
[q] = sair

=> """

saldo: float = 0
numero_saques: int = 0
limite: int = 500
LIMITE_SAQUES: int = 5
extrato: list[str] = []

while True:
    
    opcao: str = input(menu)

    if opcao == "d":
        valor_depositado: float = float(input("Digite o valor a ser depositado: "))
        saldo += valor_depositado
        extrato.append(f'Deposito: R$ {valor_depositado:.2f}')
        print(f'\nDeposito de R$ {valor_depositado:.2f} efetuado com sucesso!')
    
    elif opcao == "s":
        valor: float = float(input("Digite o valor que deseja sacar: "))

        if  valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f}")
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == 'e':
        print("\n================ EXTRATO ================")
        if extrato != []:
            for operação in extrato:
                print(operação)
        else:
            print("Não foram realizadas movimentações.")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    
    elif opcao == "q":
        break

    

