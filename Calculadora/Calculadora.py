from operators import soma, subtracao, multiplicacao, divisao
from user_input import option, input_values, new
import os

op = option()

n1, n2 = input_values()

if op == 1:
    total  = soma(n1, n2)
    print(f"O total da soma entre {n1} e {n2} é {total}")
elif op == 2:
    total  = subtracao(n1, n2)
    print(f"O total da subtracao entre {n1} e {n2} é {total}")
elif op == 3:
    total  = multiplicacao(n1, n2)
    print(f"O total da multiplicação entre {n1} e {n2} é {total}")
else:
    total  = divisao(n1, n2)
    print(f"O total da divisão entre {n1} e {n2} é {total}")
print("Deseja fazer outro calculo?")
new()

