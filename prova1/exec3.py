from __future__ import unicode_literals
# -*- coding: utf-8 -*-
#linha 2: definição de uma função chamada triplo
#linha 2: comando de impressão
#linha 3: comando de retorno
#linha 5: definição de uma função chamada subtraindo
#linha 6: comando de impressão
#linha 7: comando de retorno
#linha 9: estrutura de decisão com duas condições and. Ambas as condições precisam ser maior que 0 para que essa estrutura de desição seja aceita
#linha 10: comando de impressão
#linha 11: estrutura de decisão contrária à da linha 9
#linha 12: comando de impressão
#
#
#fluxo de execução
#Triplicando, resultado: 30
#Subtraindo, resultado: 1
#Triplicando, 15
#Subtraindo, -38
#entrou no else

def triplo(x):
    print "Triplicando, resultado: {}".format(x*3)
    return x*3

def subtraindo(x, y):
    print "Subtraindo, resultado: {}".format(x-y)
    return x-y

if subtraindo(31, triplo(10)) > 0 and subtraindo(-23, triplo(5)) > 0:
    print "Entrou no if"
else:
    print "Entrou no else"
