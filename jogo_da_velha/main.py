from time import sleep
import random

class Tabuleiro:
    def __init__(self, eixo_x, eixo_y):
        self.eixo_x = eixo_x
        self.eixo_y = eixo_y

    def criar_tabuleiro(self, eixo_x, eixo_y):
        return [[" "] * self.eixo_x for _ in range(self.eixo_y)]

    def limpar_tabuleiro(self):
        pass

class Jogador:
    def __init__(self, nome,  simbolo):
        self.nome = nome
        self.simbolo = simbolo

simbolos = ["0","X"]
comecar = input('Digite [1] para começar [0] para sair: ')
nome_jogador = input('Qual é o seu nome? ')
print("Vejamos com qual simbolo você irá jogar...")
sleep(1)
simbolo_jogador = random.choice(simbolos)
if simbolo_jogador == "0":
    print("Você será o de simbolo 0. Portanto começará a partida")
else:
    print("Você será o de simbolo X, Portanto jogará depois do computador")

Jogador(nome_jogador, simbolo_jogador)

#tab = Tabuleiro(3, 3)
#print(tab.criar_tabuleiro(3, 3))