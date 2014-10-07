

import random
# Jogo de Craps. Faca um programa de implemente um jogo de Craps. O jogador
# lanca um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada,
# voce tirar 7 ou 11, voce tirou um "natural" e ganhou. Se voce tirar 2, 3 ou
# 12 na primeira jogada, isto e chamado de "craps" e voce perdeu. Se, na
# primeira jogada, voce fez um 4, 5, 6, 8, 9 ou 10,este e seu "Ponto". Seu
# objetivo agora e continuar jogando os dados ate tirar este numero novamente.
# Voce perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
# Dica: para simular o lancamento do dado, utilize o metodos Random do Python.!


def lancar_dados():
    return random.randint(2, 12)


entrada = ""
jogada = 0
ponto = 0
print "digite  \"sair\" para sair (sem aspas)\naperte <enter> para rolar os dados: "

while (entrada!="sair"):
    jogada += 1
    print "Jogada {}".format(jogada)
    entrada = raw_input("Esperando acao: ")

    if entrada == "sair":
        print "Saindo do jogo... Tchau"
    else:
        if jogada>1:
            print "Seu ponto e {}".format(ponto)
        valor = lancar_dados()
        print "O valor do dado e {}\n\n".format(valor)
        if jogada == 1:
            if valor == 7 or valor == 11:
                print "Voce tirou um natural e ganhou, PARABENS"
                exit()
            elif valor == 2 or valor == 3 or valor == 12:
                print "Voce tirou um craps e perdeu, melhor sorte da proxima vez"
                exit()
            else:
                ponto = valor
        else:
            if valor == 7:
                print "Voce tirou um 7 antes de repetir seu ponto, voce perdeu"
                exit()
            elif ponto == valor:
                print "Voce conseguiu repetir seu ponto e ganhou, Parabens"
                exit()

