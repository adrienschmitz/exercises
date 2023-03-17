minutos_assitidos = [60, 120]
assinantes = [True, False]

minutos_n = []
total_minutos = 0

for i in range(len(assinantes)):
    total_minutos += minutos_assitidos[i]
    if assinantes[i] == True:
        minutos_n.append(minutos_assitidos[i] * 2)
        
print(total_minutos)
print(minutos_n)

    