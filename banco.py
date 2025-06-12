

extrato = ''
contsaq= 0 
total= 0
saque= 0
deposito= 0
while True:
    menu = input(""""
    [1]Depósito
    [2]Saque
    [3]Extrato
    [4]Sair
"""
)

    if menu =="1":
        deposito = float(input('\n Quanto deseja depositar?\nR$'))
        total += deposito
        extrato += (f'\n Depósito:R${deposito:.2f}')
    elif menu =="2":
        if contsaq == 3:
            print('\n Limite de saques excedido')
            print(f'\n O seu extrato é: {extrato}\n Saldo:{total}')
        else:
            saque = float(input('\n Quanto deseja sacar?\nR$'))
            if saque>500:
                print('\n Limite máximo é de R$500,00')
            elif saque>total:
                print('\n Valor maior do que o saldo')
            else:
                contsaq += 1
                total -= saque
                extrato += (f'\n Sacado:R${saque:.2f}')
    elif menu== "3":
        print(f'\n O seu extrato é: R${extrato:.2f}\n Saldo:R${total:.2f}')
    else:
        print('Saindo do sistema...')
        break



