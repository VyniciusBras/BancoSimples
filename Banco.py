def caixa_eletronico():
    contacorrente = [0] * 10
    saldo = [0.0] * 10
    i = 0

    while i < 10:
        print("\nCartão inserido, favor digite sua conta corrente: ")
        contacorrente[i] = int(input()) 
        saldo[i] = 0.0

        while True:
            print("\n--Escolha a opção desejada!--")
            print(" 1 - Saldo")
            print(" 2 - Saque")
            print(" 3 - Depósito")
            print(" 4 - Sair")
            op = int(input("Escolha a opção desejada: "))

            if op == 1:
                print(f"\nSeu saldo é: {saldo[i]:.2f}")
            elif op == 2:
                saque = float(input("\nDigite a quantia você gostaria de sacar: "))
                if saque <= saldo[i]:
                    print(f"\nVocê sacou: {saque:.2f}")
                    saldo[i] -= saque
                else:
                    print("\nSaldo insuficiente!")
            elif op == 3:
                deposit = float(input("\nDigite a quantia que deseja de depositar: "))
                print(f"\nVocê depositou: {deposit:.2f}")
                saldo[i] += deposit
            elif op == 4:
                print(f"\nNúmero de sua conta corrente: {contacorrente[i]}")
                print(f"\nSeu saldo atual é: {saldo[i]:.2f}")
                print("\nObrigado pela preferência, volte sempre!")
                i += 1
                break
            else:
                print("\nOpção inválida!")

    print("\nRelatório!")
    for j in range(i):
        print(f"\nConta: {contacorrente[j]}")
        print(f"Saldo: {saldo[j]:.2f}")

if __name__ == "__main__":
    caixa_eletronico()

 
