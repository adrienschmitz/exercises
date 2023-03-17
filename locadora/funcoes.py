from num2words import num2words

def listaCarrosDisponiveis(carros):
    for key, carro in enumerate(carros):
        print(f"[{key}] {carro[0]} - R${carro[1]} /dia")


def listaCarrosAlugados():
    for key, carro in enumerate(carros_alugados):
        print(f"[{key}] {carro[0]}")


def alugaCarro(carros, carro, dias):
    print(f"Você escolheu {carros[carro][0]} pelo valor de R${carros[carro][1]}")
    if dias > 1:
        print(f"Voce deverá pagar R${dias*carros[carro][1]} pelos {num2words(dias, lang='pt-br', to='cardinal')} dias que reservou")
    else:
        print(f"Voce deverá pagar R${dias*carros[carro][1]} pelo {num2words(dias, lang='pt-br', to='cardinal')} dia que reservou")
    

def devolveCarro(carro):
    carros_disponiveis.append(carros_alugados.pop(devolucao))

    print(carros_alugados)
    print("====================")
    print(carros_disponiveis)