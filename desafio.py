historico_deposito = []
historico_saques = []
limite_saque = 3
saldo = 2000.00
menu_title = " SISTEMA BANCÁRIO PYTHON "
menu = """
Selecione a opção que deseja acessar:
    [1] Depositar Valor
    [2] Sacar Valor
    [3] Exibir Extrato
    [0] Sair
"""
while True:
    print("##################################################")
    print(menu_title.center(50,"#"))
    print("##################################################")
    op = int(input(menu))
    
    
    match op:
        case 1:
            print("-------------------------------------")
            print("---------- DEPOSITAR VALOR ----------")
            print("-------------------------------------")
            deposito = float(input("Insira o valor que queira depositar: "))
            saldo += deposito
            historico_deposito.append(f"R$ {deposito:.2f}")
            print(f"Deposito de R$ {deposito:.2f} realizado")
            print(historico_deposito)
            
            
        case 2:
            print("-------------------------------------")
            print("---------- SACAR VALOR ----------")
            print("-------------------------------------")
            if(limite_saque == 0):
                print()
                print("não é possível realizar saque, limite de saques diários excedido!")
                print()     
            else:
                saque = float(input("Insira o valor que queira sacar: "))
                if(saque > 500):
                    print("Não foi possível sacar, valor máximo de R$ 500,00 excedido")
                else:
                    saldo -= saque
                    limite_saque -= 1
                    print(f"saque de R$ {saque:.2f} realizado")
        case 3:
            print("-------------------------------------")
            print("---------- EXIBIR EXTRATO ----------")
            print("-------------------------------------")
        case 0:
            break
        case _:
            print("Opção invalida, por farvor escolha uma correta")
            print("-------------------------------------")
    
        