import os

def option():
    print("Que operação deseja fazer? ")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")
    try:
        opcao = int(input("Opção: "))
        if opcao in [0, 1, 2, 3, 4]:
            return opcao
        else:
            os.system('cls') or None
            opcao = input("Digite uma opção válida: ")
            option()
    except ValueError:
        os.system('cls') or None
        print("Não é um numero. Digite uma opção válida")
        option()


def input_values():
    while True:
        try:
            num_1 = int(input("Digite o primeiro numero: "))
            num_2 = int(input("Digite o segundo numero: "))
            return num_1, num_2
        except ValueError:
            print("Valor informado não é um inteiro")

def new():
    opcao = input("Opção: ")[0].lower()
    if opcao in ["s"]:
        os.system('cls') or None
        option()
    else:
        os.system('cls') or None
        print("Obrigado, volte sempre")

