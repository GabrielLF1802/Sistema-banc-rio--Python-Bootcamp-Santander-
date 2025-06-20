def saque(valor,saldo,extrato):
        global contsaq
        limite_saques= 500
        if contsaq == 3:
            print('\n Limite de saques excedido')
            print(f'\n O seu extrato é: {extrato}\n Saldo:{saldo}')
        else:
            if valor>limite_saques:
                print('\n Limite máximo é de R$500,00')
            elif valor>saldo:
                print('\n Valor maior do que o saldo')
            else:
                contsaq += 1
                saldo -= valor
                extrato += (f'\n Sacado:R${valor:.2f}')
        return saldo, extrato

def deposito(saldo, valor, extrato):
    saldo += valor
    extrato += (f'\n Depósito:R${valor:.2f}')
    return extrato, saldo

def res_extrato(saldo,*,extrato):
    print(f'\n O seu extrato é:{extrato}\n Saldo:R${saldo:.2f}')


def criarUsu(usuarios):
    cpf= int(input('Digite o cpf'))
    usuario= verificarusu(cpf, usuarios)

    if usuario:
        print('Já existe esse usuario')
        return 
    nome= input('Digite o nome')
    nasc= input("Digite o nasc")
    end= input('Digite o end')

    usuarios.append({"nome":nome, "nasc": nasc,"end": end, "cpf":cpf})
    print("Usuário criado com sucesso")

def criarcont(agencia, numeroconta, usuarios):
    cpf= int(input('Informe o cpf'))
    usuario= verificarusu(cpf,usuarios)

    if usuario:
        print('Esse usuário já existe, conta criada com sucesso')
        return {"agencia": agencia, "numeroconta": numeroconta, "usuario":usuario}
    print('Usuário não encontrado')


def verificarusu(cpf,usuarios):
    filtro = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return filtro[0] if filtro else None



extrato = ''
usuarios= []
contas=[]
contsaq= 0 
saldo= 0
valor= 0
agencia =101
while True:
    menu = input(""""
    [1]Depósito
    [2]Saque
    [3]Extrato
    [4]Sair
    [5]Novo Usuário
    [6]Nova Conta
    [7]Listar contas
"""
)
    print(usuarios)
    if menu =="1":
        valor = float(input('\n Quanto deseja depositar?\nR$'))
        extrato, saldo = deposito(saldo, valor, extrato)
    elif menu =="2":
        valor= float(input('Digite o valor que deseja sacar'))
        saldo, extrato= saque(valor=valor, saldo=saldo, extrato=extrato)
    elif menu== "3":
        extrato= res_extrato(saldo,extrato=extrato)
    elif menu=="5":
        criarUsu(usuarios)
    elif menu=="6":
        numeroconta= len(contas)
        conta = criarcont(agencia,numeroconta,usuarios)
        if conta:
            contas.append(conta)
    elif menu=="7":
        print(contas)
    else:
        print('Saindo do sistema...')
        break



