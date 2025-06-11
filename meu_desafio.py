#Criar um menu
menu = """
====== MENU ======
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
==================
"""

#Criar variáveis principais
saldo = 0.0
extrato = ""
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

opcao = ""
MENSAGEM_INVALIDO = "Valor inválido! Só aceitamos valores positivos."

#Criar um laço de repetiçao
#Dentro do laço, criar as opções de depósito, saque e extrato

while opcao != "q":
    print(menu)
    opcao = input("Escolha uma opção: ")

    # DEPÓSITO
    if opcao == "d":
        deposito = float(input("Informe o valor do depósito: R$ "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n"
            print("Deposito no valor de R$ {:.2f} realizado com sucesso!".format(deposito))
        else:
         print(MENSAGEM_INVALIDO)
    # SAQUE
    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            saques = float(input("Informe o valor do saque: R$ "))
            if saques > saldo:
                print ("Não será possível sacar o dinheiro por falta de saldo")
            elif saques > limite:
                print("O valor do saque não pode ser maior que R$ {:.2f} !".format(limite))
            elif saques <= 0:
                print (MENSAGEM_INVALIDO)
            elif LIMITE_SAQUES == numero_saques:
                print("Número máximo de saques diáriosd atingido!")
            else:
                saldo -= saques
                extrato += f"saques: R$ {saques:.2f}\n"
                numero_saques += 1
                print("Saque no valor de R$ {:.2f} realizado com sucesso!".format(saques))  
        else:
                print("Número máximo de saques diários atingido!")     
    elif opcao == "e":
        print ("====== EXTRATO ======")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
            print(f"Saldo: R$ {saldo:.2f}")
    elif opcao == "q":
        print("Obrigado por utilizar nossos serviços! Até logo!")
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")  
