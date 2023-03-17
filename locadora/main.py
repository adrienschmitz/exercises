from funcoes import listaCarrosAlugados, listaCarrosDisponiveis, alugaCarro, devolveCarro

carros_disponiveis = [
    ["Chevrolet Tracker", 120],
    ["Chevrolet Onix", 90],
    ["Chevrolet Spin", 150],
    ["Hyundai HB20", 85],
    ["Hyundai Tucson", 120],
    ["Fiat Uno", 60],
    ["Fiat Mobi", 70],
    ["Fiat Pulse", 130],
]

carros_alugados = []

print('====================')
print('Bem vindo a Locadora')
print('====================')

print('O que deseja fazer?')
print("0 - Mostrar Portfólio | 1 - Alugar um carro | 2 Devolver um carro")
option = int(input())
i = 0

if option == 0:
    listaCarrosDisponiveis(carros_disponiveis)
elif option == 1:
    escolha = int(input("Qual o carro da sua preferencia? "))
    dias = int(input("Por quantos dia pretende alugar? "))
    alugaCarro(carros_disponiveis, escolha, dias)
    carros_alugados.append(carros_disponiveis.pop(escolha))

elif option == 2:
    listaCarrosAlugados()
    devolucao = int(input("Qual carro deseja devolver? "))
    devolveCarro(devolucao)

